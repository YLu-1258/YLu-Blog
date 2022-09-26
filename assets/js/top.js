var mybutton = document.getElementById("Top");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    mybutton.style.display = "block";
} 
else {
    mybutton.style.display = "none";
}
}

function scrollToTop() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}