const { app, BrowserWindow } = require('electron');
const path = require('path');
require('dotenv').config();

const axios = require('axios');


const debugMode = process.env.DEBUG_MODE === 'true';

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'src', 'preload.js')
    },
    // frame: false,
    // titleBarStyle: 'hidden',
    titleBarOverlay: {
      color: '#2f3241',
      symbolColor: '#74b1be',
      height: 60
    },
  });

  mainWindow.loadFile(path.join(__dirname, 'src', 'index.html'));

  if (debugMode) {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', function () {
    mainWindow = null;
  });

  console.log('API URL:', process.env.API_URL);
  console.log('DEBUG MODE:', process.env.DEBUG_MODE);
}

app.whenReady().then(createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
  if (mainWindow === null) createWindow();
});
