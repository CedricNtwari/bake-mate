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
    if (scrollUpButton) {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollUpButton.style.display = 'block';
        } else {
            scrollUpButton.style.display = 'none';
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const editedIngredientIds = []; // List to store edited ingredient IDs

    const editButtons = document.querySelectorAll('.edit-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const editPanel = this.nextElementSibling;
            editPanel.classList.toggle('show-edit-panel');

            const ingredientItem = this.closest('.ingredient-item');

            ingredientItem.classList.toggle('edit-panel-active', editPanel.classList.contains('show-edit-panel'));

            // Extract ingredient ID from the data-attribute
            const ingredientId = ingredientItem.dataset.ingredientId;

            if (editPanel.classList.contains('show-edit-panel') && !editedIngredientIds.includes(ingredientId)) {
                editedIngredientIds.push(ingredientId);
            }
        });
    });

    const updateButtons = document.querySelectorAll('.update-btn');

    updateButtons.forEach(button => {
        button.addEventListener('click', function () {
            const editPanel = this.parentElement;
            const inputField = editPanel.querySelector('.edit-input');
            const ingredientItem = this.closest('.ingredient-item');

            const newQuantity = parseFloat(inputField.value.trim());

            if (!isNaN(newQuantity) && inputField.value.trim() !== '') {
                const quantityNameSpan = ingredientItem.querySelector('.ingredient-quantity-name');
                const currentIngredient = quantityNameSpan.textContent;
                const updatedIngredient = currentIngredient.replace(/\d+(\.\d+)?/, newQuantity);
                quantityNameSpan.textContent = updatedIngredient;

                const ingredientId = ingredientItem.dataset.ingredientId;
                if (!editedIngredientIds.includes(ingredientId)) {
                    editedIngredientIds.push(ingredientId);
                }
                editPanel.classList.remove('show-edit-panel');
                inputField.value = '';

            } else {
                alert('Please enter a valid number.');
            }
        });
    });

    // Disable edit button for items without a number in the text
    disableEditButtonsForNonNumericItems();

    const updateAllButton = document.querySelector('.update-all-btn');

    if (updateAllButton) {
        updateAllButton.addEventListener('click', updateAllIngredients);
    }

    function updateAllIngredients() {
        if (editedIngredientIds.length > 0) {
            // Calculate the average change in quantity
            let totalChange = 0;
    
            // Iterate through all ingredients to calculate total change
            const allIngredientItems = document.querySelectorAll('.ingredient-item');
            allIngredientItems.forEach(item => {
                const originalQuantityText = item.querySelector('.ingredient-quantity-name').textContent.trim();
                const originalQuantity = parseFloat(originalQuantityText);
    
                if (!isNaN(originalQuantity)) {
                    const editPanel = item.querySelector('.edit-panel');
                    const inputField = editPanel.querySelector('.edit-input');
                    const newQuantity = parseFloat(inputField.value.trim());
    
                    if (!isNaN(newQuantity)) {
                        totalChange += newQuantity - originalQuantity;
                    }
                }
            });
    
            // Apply the average change proportionally to all ingredients
            allIngredientItems.forEach(item => {
                const quantityNameSpan = item.querySelector('.ingredient-quantity-name');
                const originalText = quantityNameSpan.textContent.trim();
    
                // Extract the unit (e.g., "tsp") from the original text
                const unitMatch = originalText.match(/[^\d]+/);
                const unit = unitMatch ? unitMatch[0] : '';
    
                // Extract the numeric value from the original text
                const originalValue = parseFloat(originalText);
    
                // Check if the original value is a valid number
                if (!isNaN(originalValue)) {
                    // Calculate the new quantity based on the average change
                    const averageChange = totalChange / allIngredientItems.length;
                    const newValue = originalValue + averageChange;
                    const updatedIngredientText = `${newValue.toFixed(0)} ${unit}`;
                    quantityNameSpan.innerHTML = `<span class="updated-amount">${updatedIngredientText}</span>`;
    
                    console.log(`Updated ingredient in ID ${item.dataset.ingredientId}`);
                }
            });
    
            // Clear the list of edited ingredient IDs
            editedIngredientIds.length = 0;
    
            // Toggle back the edit panel for each edited ingredient
            const editedIngredientPanels = document.querySelectorAll('.ingredient-item.edit-panel-active .edit-panel');
            editedIngredientPanels.forEach(panel => {
                panel.classList.remove('show-edit-panel');
            });
    
            // Remove the edit-panel-active class from all ingredient items
            allIngredientItems.forEach(item => {
                item.classList.remove('edit-panel-active');
            });
    
            // Disable edit buttons for items without a number in the text
            disableEditButtonsForNonNumericItems();
    
            alert('Ingredients updated will be in green!');
        } else {
            alert('No ingredients have been edited.');
        }
    }
    
            

    // Get the input field and search button
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');

    // Add event listener for "Enter" key press
    searchInput.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            // Simulate a click on the search button
            searchButton.click();
        }
    });

    // Helper function to disable edit buttons for items without a number in the text
    function disableEditButtonsForNonNumericItems() {
        const ingredientItems = document.querySelectorAll('.ingredient-item');

        ingredientItems.forEach(item => {
            const quantityNameSpan = item.querySelector('.ingredient-quantity-name');
            const hasNumber = /\d/.test(quantityNameSpan.textContent);

            const editButton = item.querySelector('.edit-btn');
            editButton.disabled = !hasNumber;
        });
    }
});


