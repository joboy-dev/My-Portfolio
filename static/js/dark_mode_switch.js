var darkModeSwitch = document.querySelector('.dark-mode')
var root = document.querySelector(':root')

var heroSection = document.querySelector('#hero')

var darkColor = '#004643'
var lightColor = '#ffffff'

function toggleDarkMode() {
    var darkModeIcon = document.getElementById('dark-mode-icon')

    if (root.style.getPropertyValue("--background-dark") == darkColor) {
        // Switch to dark mode
        root.style.setProperty("--background-dark", lightColor);
        root.style.setProperty("--text-dark", darkColor);
        
        root.style.setProperty("--background-light", darkColor);
        root.style.setProperty("--text-light", lightColor);

        darkModeIcon.classList.remove('fa-moon')
        darkModeIcon.classList.add('fa-sun')

        heroSection.classList.remove('light-theme-background')
        heroSection.classList.add('dark-theme-background')

        return true
    } else {
        // Switch to light mode
        root.style.setProperty("--background-dark", darkColor);
        root.style.setProperty("--text-dark", lightColor);
        
        root.style.setProperty("--background-light", lightColor);
        root.style.setProperty("--text-light", darkColor);

        darkModeIcon.classList.remove('fa-sun')
        darkModeIcon.classList.add('fa-moon')

        heroSection.classList.remove('dark-theme-background')
        heroSection.classList.add('light-theme-background')

        return false
    }
}

darkModeSwitch.addEventListener('click', () => {
    toggleDarkMode()
});
