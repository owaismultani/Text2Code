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



