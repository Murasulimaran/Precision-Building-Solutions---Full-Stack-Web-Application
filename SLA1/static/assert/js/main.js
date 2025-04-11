const openMenu = document.getElementById('menu');
const showMenu = document.querySelector('.showmenu');

openMenu.addEventListener('click', function(){
    if(showMenu.style.display == 'block'){
        showMenu.style.display = 'none';
    }
    else {
        showMenu.style.display = 'block';
    }
});


const chatMe = document.getElementById("chat-me");
const openForm = document.getElementById("open-form");
const cancelForm = document.getElementById("cancel-form");

chatMe.addEventListener("click", function(event){
    event.preventDefault();

    chatMe.style.display = "none";
    openForm.style.display = "block";
});

cancelForm.addEventListener("click", function(){
    openForm.style.display = "none";
    chatMe.style.display = "inline-block";
});