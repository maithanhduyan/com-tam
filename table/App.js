import React, { useState, useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import axios from 'axios';

export default function App() {
  const [menu, setMenu] = useState([]);

  useEffect(() => {
    // Gửi yêu cầu GET đến API và cập nhật menu khi nhận được dữ liệu
    axios.get('https://10.220.56.18/api/menu')

      .then(response => {
        setMenu(response.data); // Cập nhật menu với dữ liệu nhận được từ API
      })
      .catch(error => {
        console.error('Error fetching menu:', error);
      });
  }, []); // [] đảm bảo rằng useEffect chỉ chạy một lần sau khi component được render

  return (
    <View style={styles.container}>
      <Text>Table App</Text>
      {/* Hiển thị danh sách menu */}
      {menu.map(item => (
        <Text key={item.item_id}>{item.item_name} Giá: {item.price} vnđ</Text>
      ))}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
