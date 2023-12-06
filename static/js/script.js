function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// Show/hide the scroll-up button based on scroll position
window.onscroll = function() {
    showScrollUpButton();
};

function showScrollUpButton() {
    var scrollUpButton = document.querySelector('.scroll-up-btn');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollUpButton.style.display = 'block';
    } else {
        scrollUpButton.style.display = 'none';
    }
}