console.log('Renderer process is working!');


// document.addEventListener('DOMContentLoaded', () => {
//     // Gửi yêu cầu HTTP để lấy danh sách menu từ localhost:5000/api/menu
//     axios.get('http://localhost:5000/api/menu')
//         .then(response => {
//             const menuItems = response.data; // Danh sách menu nhận được từ API
//             console.log(menuItems);
//             // Hiển thị danh sách menu lên màn hình
//             const menuContainer = document.getElementById('menu-container');
//             menuItems.forEach(item => {
//                 const menuItem = document.createElement('div');
//                 menuItem.textContent = item.item_name;
//                 menuContainer.appendChild(menuItem);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching menu:', error);
//         });
// });

