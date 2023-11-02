// foot
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
if (
  document.body.scrollTop > 10 ||
  document.documentElement.scrollTop > 10
) {
  // 显示返回顶部按钮
  document.getElementById("backToTopBtn").style.display = "block";
} else {
  // 隐藏返回顶部按钮
  document.getElementById("backToTopBtn").style.display = "none";
}
}

// 平滑滚动到页面顶部
function scrollToTop() {
document.body.scrollTop = 0; // Safari
document.documentElement.scrollTop = 0; // Chrome, Firefox, IE and Opera
}