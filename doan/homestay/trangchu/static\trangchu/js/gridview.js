$(document).ready(function() {
    $('#list').click(function(event){event.preventDefault();$('#products .item').addClass('list-group-item');});
    $('#grid').click(function(event){event.preventDefault();$('#products .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');});
});
// Lấy phần tử thanh kéo giá tiền và nhãn hiển thị giá trị
const priceRange = document.getElementById('priceRange');
const priceValue = document.getElementById('priceValue');

// Xử lý sự kiện khi di chuyển thanh kéo
priceRange.addEventListener('input', function() {
    // Lấy giá trị hiện tại của thanh kéo
    const value = priceRange.value;
    // Cập nhật giá trị hiển thị của giá tiền
    priceValue.textContent = value;
});
