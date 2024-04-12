var expandedWidth = "250px";
var collapsedWidth = "80px";
var buttonCollapsedWidth = "35px";
var buttonExpandedWidth = "200px";

function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var content = document.getElementsByClassName("main-content")[0];
    var toggleIcon = document.getElementById("toggleIcon");
    var button = document.getElementById("sidebarCollapse");

    sidebar.classList.toggle("collapsed");

    if (sidebar.classList.contains("collapsed")) {
        content.style.marginLeft = collapsedWidth;
        button.style.left = buttonCollapsedWidth;
        toggleIcon.innerHTML = "chevron_right";
        // Optionally hide chat names and items here if you want more control
    } else {
        content.style.marginLeft = expandedWidth;
        button.style.left = buttonExpandedWidth;
        toggleIcon.innerHTML = "chevron_left";
        // Optionally show chat names and items here if you hide them explicitly in JS
    }
}

function toggleDropdown() {
    var sidebar = document.getElementById("sidebar");
    var dropdown = document.querySelector('.dropdown-menu');

    // Check if the sidebar is collapsed
    if (sidebar.classList.contains("collapsed")) {
        var button = document.getElementById("sidebarCollapse");
        var toggleIcon = document.getElementById("toggleIcon");
        // Logic to expand the sidebar
        sidebar.classList.remove("collapsed");
        button.style.left = buttonExpandedWidth;
        toggleIcon.innerHTML = "chevron_left";
    }
    // Toggle the dropdown visibility
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}
