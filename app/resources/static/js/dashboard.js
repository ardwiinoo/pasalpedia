function toggleDropdown(menuId) {
    const dropdown = document.getElementById('dropdown-' + menuId);
    const icon = document.getElementById('icon-' + menuId);

    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.style.display = 'block';
        icon.classList.remove('rotate-90');
    } else {
        dropdown.style.display = 'none';
        icon.classList.add('rotate-90');
    }
}