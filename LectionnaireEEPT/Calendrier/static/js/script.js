
const btn_menu = document.querySelector('#img_menu')

btn_menu.addEventListener('click', () => {
    const menu = document.querySelector('#nav_bar_link');
    const isMenuVisible = menu.style.display === 'flex';
    menu.style.display = isMenuVisible ? 'none' : 'flex';
    menu.setAttribute('aria-expanded', !isMenuVisible);
})