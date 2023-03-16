/**
 * @author Aman Raj
 * @since 21/02/2023
 * @encoding utf-8
*/


function verify_sound() {
  var verify = new Audio("verify.mp3");
  verify.play();
}

function error_sound() {
  var error = new Audio("error.mp3");
  error.play();
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function alertType() {
  alert("Sentence is Too short");
}

async function getLength() {
  const MAX_VALUE = 10;

  var textArea = document.getElementById("input");
  var length = textArea.value.length;
  var submission = document.getElementById("result");
  var text_verifier = document.getElementById("submission_text");

  if (length >= MAX_VALUE) {
    submission.setAttribute("style", "border-left: thick double #4BB543;");
    text_verifier.innerText = "Data Submited SuccessFully";
    verify_sound();
  } else {
    submission.setAttribute("style", "border-left: thick double #FC100D;");
    text_verifier.innerText = "Length Error: Length of Sentence is Too Short";
    error_sound();
    await sleep(1);
    alertType();
  }
}


