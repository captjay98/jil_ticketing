let nav = document.querySelector('.header .nav');

document.querySelector('#menu-btn').onclick = () =>{
    nav.classList.toggle('active');
}

window.onscroll = () =>{
    nav.classList.remove('active');
}

document.querySelectorAll('.about .video-container .controls .control-btn').forEach(btn =>{
    btn.onclick = () =>{
        let src = btn.getAttribute('data-src');
        document.querySelector('.about .video-container .video').src = src;
    }
})