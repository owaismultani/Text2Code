document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.querySelector('.mdc-select');

    // Initialize MDC Select component
    let mdcSelect = mdc.select.MDCSelect.attachTo(selectElement);

    function updateLanguages(selectedValue) {
        fetch('/languages/')
            .then(response => response.json())
            .then(data => {
                const languages = data.languages;
                const selectMenu = selectElement.querySelector('.mdc-select__menu .mdc-list');
                selectMenu.innerHTML = ''; // Clear existing options
                languages.forEach(lang => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('mdc-list-item');
                    listItem.setAttribute('role', 'option');
                    listItem.setAttribute('data-value', lang.value);
                    listItem.textContent = lang.name;
                    selectMenu.appendChild(listItem);
                });

                // Properly destroy and re-initialize MDC Select with new items
                mdcSelect.destroy();
                mdcSelect = mdc.select.MDCSelect.attachTo(selectElement);

                // Set the selected value
                if (selectedValue) {
                    mdcSelect.value = selectedValue;
                }
            })
            .catch(error => console.error('Error loading languages:', error));
    }

    // Update languages and set selected value, for example 'javascript'
    updateLanguages('javascript');

    // Listen for selection changes
    mdcSelect.listen('MDCSelect:change', () => {
        console.log('Selected language:', mdcSelect.value);
    });
});


function cancelEdit(editIcon, displayName, editForm, inputField) {
    // Revert to the non-editing state
    editIcon.style.display = 'inline-block';
    displayName.style.display = 'block';
    editForm.style.display = 'none';
    inputField.readOnly = true;
    inputField.blur(); // Remove focus from the input field
}

function makeEditable() {
    const editIcon = document.querySelector('.edit-chat-button');
    const chatItem = editIcon.closest('.chat-item');
    const displayName = chatItem.querySelector('.chat-name-display');
    const editForm = chatItem.querySelector('.chat-edit-form');
    const inputField = editForm.querySelector('.chat-name-input');

    // Hide the display name and show the input field
    displayName.style.display = 'none';
    editForm.style.display = 'block';
    inputField.readOnly = false;
    editIcon.style.display = 'none';
    inputField.focus();
    inputField.setSelectionRange(inputField.value.length, inputField.value.length);

    // Add event listener for ESC key to cancel editing
    document.addEventListener('keydown', function(event) {
        if (event.key === "Escape") {
            cancelEdit(editIcon, displayName, editForm, inputField);
        }
    });

    // on enter submit the form
    inputField.addEventListener('keydown', function(event) {
        if (event.key === "Enter") {
            editForm.submit();
        }
    });

}
