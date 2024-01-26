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
                const newQuantity = inputField.value.trim();
                const currentIngredient = quantityNameSpan.textContent;
                const updatedIngredient = currentIngredient.replace(/\d+(\.\d+)?/, newQuantity);
                quantityNameSpan.textContent = updatedIngredient;
                editPanel.classList.remove('show-edit-panel');
            }
        });
    });

    const updateAllButton = document.querySelector('.update-all-btn');
    updateAllButton.addEventListener('click', updateAllIngredients);

    function updateAllIngredients() {
        // Get the edited ingredient details
        const editedIngredientId = getEditedIngredientId();
        const editedIngredientQuantity = getEditedIngredientQuantity();
    
        // Get all ingredient items
        const ingredientItems = document.querySelectorAll('.ingredient-item');
    
        // Loop through each ingredient item
        ingredientItems.forEach(item => {
            // Get the ingredient ID and quantity
            const ingredientId = item.getAttribute('data-ingredient-id');
            const quantityNameSpan = item.querySelector('.ingredient-quantity-name');
    
            // Get the original quantity and units
            const originalQuantityText = quantityNameSpan.textContent.trim();
            const originalQuantity = parseFloat(originalQuantityText);
    
            // Check if the quantity is a valid number
            if (!isNaN(originalQuantity)) {
                // Calculate the new quantity for the ingredient using the conversion factor
                const newQuantity = originalQuantity * (editedIngredientQuantity / originalQuantity);
    
                // Replace the quantity in the span
                const updatedIngredient = originalQuantityText.replace(originalQuantity, newQuantity.toFixed(1));
                quantityNameSpan.textContent = updatedIngredient;
            }
        });
    
        console.log('Update All Ingredients');
    }
    
    function getEditedIngredientId() {
        const activeEditButton = document.querySelector('.edit-btn.show-edit-panel');
        if (activeEditButton) {
            return activeEditButton.closest('.ingredient-item').dataset.ingredientId;
        }
        return null;
    }
    

    function getEditedIngredientQuantity() {
        return parseFloat(document.querySelector('.edit-input').value);
    }

    function calculateConversionFactor(editedIngredientId, editedIngredientQuantity) {
        return 1;
    }

    function updateIngredient(ingredientId, newQuantity) {
        const editedIngredient = document.querySelector(`[data-ingredient-id="${ingredientId}"]`);
        const editedIngredientQuantityName = editedIngredient.querySelector('.ingredient-quantity-name');
        editedIngredientQuantityName.textContent = newQuantity;
    }
});