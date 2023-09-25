var navbar = document.querySelector('.navbar')
var body = document.querySelector('.body')

var cancel = document.querySelector('.navbar .cancel-icon')
var menu = document.querySelector('#content .menu-icon')
var navLinks = document.querySelectorAll('.nav-links a')

var root = document.querySelector(':root')

function closeNavbar() {
    navbar.classList.add('none')
    body.classList.remove('none')

    // body.style.display = 'block'
    // navbar.style.display = 'none'
}

function openNavbar() {
    navbar.classList.remove('none')
    body.classList.add('none')

    // body.style.display = 'none'
    // navbar.style.display = 'block'
}

if (body.classList.contains('none')) {
    root.addEventListener('click', closeNavbar)
}

menu.addEventListener('click', openNavbar)

cancel.addEventListener('click', closeNavbar)

navLinks.forEach((link) => closeNavbar)


// window.addEventListener('orientationchange', () => {
//     var mq = window.matchMedia('screen and (max-width: 1024px)');
    
//     if (mq.matches) {
//         menu.classList.remove('icon-none')
//         cancel.classList.remove('icon-none')
//     } else {
//         menu.classList.add('icon-none')
//         cancel.classList.add('icon-none')
//     }
// })

var mq = window.matchMedia('screen and (max-width: 1024px)');
    
if (mq.matches) {
    menu.classList.remove('icon-none')
    cancel.classList.remove('icon-none')
} else {
    menu.classList.add('icon-none')
    cancel.classList.add('icon-none')
}