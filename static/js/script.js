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
    const editedIngredientIds = []; // List to store edited ingredient IDs

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
            const ingredientItem = this.closest('.ingredient-item');

            if (inputField.value.trim() !== '') {
                const newQuantity = inputField.value.trim();
                const quantityNameSpan = ingredientItem.querySelector('.ingredient-quantity-name');
                const currentIngredient = quantityNameSpan.textContent;
                const updatedIngredient = currentIngredient.replace(/\d+(\.\d+)?/, newQuantity);
                quantityNameSpan.textContent = updatedIngredient;

                const ingredientId = ingredientItem.dataset.ingredientId;
                if (!editedIngredientIds.includes(ingredientId)) {
                    editedIngredientIds.push(ingredientId);
                }

                editPanel.classList.remove('show-edit-panel');
            }
        });
    });

    const updateAllButton = document.querySelector('.update-all-btn');

    if (updateAllButton) {
        updateAllButton.addEventListener('click', updateAllIngredients);
    }

    function updateAllIngredients() {
        if (editedIngredientIds.length > 0) {
            const totalEditedIngredients = editedIngredientIds.length;
    
            // Calculate the proportional adjustment factor
            const adjustmentFactor = 1 / totalEditedIngredients;
    
            // Get the details of the edited ingredients
            editedIngredientIds.forEach(ingredientId => {
                const editedIngredient = document.querySelector(`[data-ingredient-id="${ingredientId}"]`);
                const editedIngredientQuantityName = editedIngredient.querySelector('.ingredient-quantity-name');
    
                // Your logic to update each ingredient goes here
                const originalEditedText = editedIngredientQuantityName.textContent;
                const originalEditedQuantity = parseFloat(originalEditedText);
    
                // Check if the original quantity contains a number
                if (!isNaN(originalEditedQuantity)) {
                    const newEditedQuantity = originalEditedQuantity * adjustmentFactor;
                    const updatedIngredientText = originalEditedText.replace(originalEditedQuantity, newEditedQuantity.toFixed(1));
                    editedIngredientQuantityName.textContent = updatedIngredientText;
    
                    // For example, adjust all other ingredients proportionally
                    const otherIngredients = document.querySelectorAll('.ingredient-item:not([data-ingredient-id="' + ingredientId + '"])');
                    otherIngredients.forEach(otherIngredient => {
                        const otherQuantityNameSpan = otherIngredient.querySelector('.ingredient-quantity-name');
                        const originalOtherText = otherQuantityNameSpan.textContent;
                        const originalOtherQuantity = parseFloat(originalOtherText);
    
                        // Check if the original quantity contains a number
                        if (!isNaN(originalOtherQuantity)) {
                            const newOtherQuantity = (originalOtherQuantity * adjustmentFactor) + 1;
                            const updatedOtherText = originalOtherText.replace(originalOtherQuantity, newOtherQuantity.toFixed(1));
                            otherQuantityNameSpan.textContent = updatedOtherText;
                        }
                    });
    
                    console.log(`Updated ingredient with ID ${ingredientId}`);
                }
            });
    
            // Clear the list of edited ingredient IDs
            editedIngredientIds.length = 0;
    
            alert('Ingredients updated successfully!');
        } else {
            alert('No ingredients have been edited.');
        }
    }
    
});
