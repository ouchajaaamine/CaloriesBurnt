// Fonction pour définir le thème
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.setAttribute('data-theme', themeName);
    document.body.setAttribute('data-theme', themeName);
    
    // Dispatch a custom event for other scripts to listen for theme changes
    const event = new CustomEvent('themeChanged', { detail: { theme: themeName } });
    document.dispatchEvent(event);
}

// Fonction pour basculer entre le mode sombre et le mode clair
function toggleTheme() {
    if (localStorage.getItem('theme') === 'light') {
        setTheme('dark');
    } else {
        setTheme('light');
    }
}

// Fonction pour initialiser le thème au chargement de la page
function initTheme() {
    // Si l'utilisateur a déjà choisi un thème, on l'utilise
    if (localStorage.getItem('theme')) {
        setTheme(localStorage.getItem('theme'));
    } else {
        // Par défaut, on utilise le thème sombre
        setTheme('dark');
    }
    
    // Ajouter l'animation au bouton lors de l'initialisation
    setTimeout(() => {
        const themeToggle = document.querySelector('.theme-toggle');
        if (themeToggle) {
            themeToggle.classList.add('initialized');
        }
    }, 500);
}

// Initialiser le thème au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    initTheme();
    
    // Ajouter l'événement de clic sur le bouton de basculement de thème
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            toggleTheme();
            // Ajouter une animation au bouton
            this.classList.add('clicked');
            setTimeout(() => {
                this.classList.remove('clicked');
            }, 500);
        });
    }
}); 