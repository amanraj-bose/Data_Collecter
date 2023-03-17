/*
  * @author Aman Raj
  * @since 2023 
  * @encoding UTF-8
*/


function sleep(ms){
    return new Promise(
        resolve => setTimeout(resolve, ms)
    );
}

async function hamclick(){

    var button = document.getElementById("ham-bar-1");

    var cross_button = document.getElementById("ham-bar-2");

    var DropDownMenu = document.getElementById("nav-down-body-id-1");

    var Effect = document.getElementById("nav-down-body-id-1");

    button.style.display = "none";
    cross_button.style.display = "grid"; 

    DropDownMenu.style.display = "grid";

    Effect.style.transform = "translateY(0px)";
    Effect.style.transition = "all 2s";
};

function crossClick(){
    var button = document.getElementById("ham-bar-2");

    var humButton = document.getElementById("ham-bar-1");

    var DropDownMenu = document.getElementById("nav-down-body-id-1");

    button.style.display = "none";
    DropDownMenu.style.display = "none";
    humButton.style.display = "block";
}
