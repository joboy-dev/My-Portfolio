var darkModeSwitch = document.querySelector('.dark-mode')
var root = document.querySelector(':root')

var heroSection = document.querySelector('#hero')

var darkColor = '#0c1618'
var lightColor = '#f1f1f1'

// Check local storage for dark mode preference on page load
const savedDarkMode = localStorage.getItem('darkmode');
if (savedDarkMode === 'true') {
    toggleDarkMode();
}

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

        localStorage.setItem('darkmode', 'true')
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

        localStorage.setItem('darkmode', 'false')
    }
}

darkModeSwitch.addEventListener('click', toggleDarkMode);
