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

document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const editPanel = this.nextElementSibling;
            editPanel.classList.toggle('show-edit-panel');
        });
    });

    const updateButtons = document.querySelectorAll('.update-btn');

    updateButtons.forEach(button => {
        button.addEventListener('click', function () {
            const editPanel = this.parentElement;
            const inputField = editPanel.querySelector('.edit-input');
            const quantityNameSpan = this.closest('.ingredient-item').querySelector('.ingredient-quantity-name');

            if (inputField.value.trim() !== '') {
                // Update the quantity in the sentence
                const newQuantity = inputField.value.trim();
                const currentIngredient = quantityNameSpan.textContent;
                const updatedIngredient = currentIngredient.replace(/\d+(\.\d+)?/, newQuantity);
                quantityNameSpan.textContent = updatedIngredient;

                // Hide the edit panel
                editPanel.classList.remove('show-edit-panel');
            }
        });
    });
});