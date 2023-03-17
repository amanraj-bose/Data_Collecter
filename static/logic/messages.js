/**
 * @author Aman Raj
 * @since 6 March 2023
 * @copyright 2023
 * @encoding UTF-8
*/


function format(value, formater){
    return value.toString().replace('{}', formater);
}



function comming(){    
    var flash = document.getElementById("flash-about-msg");
    transforms(flash);
    display(flash);
}


function transforms(flash){
    
    let count = 0;
    for(let val = 0; val < 550; val++) {
        flash.setAttribute('style', "transform: translateX({}px)".replace('{}', val.toString()));
        count = count + 1;
        if (count == 550) {
            break;
        }
    }
}

function display(flash){
    flash.setAttribute('style', "display: none;");
}