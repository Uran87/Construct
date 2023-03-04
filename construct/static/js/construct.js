// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  	console.log(event.target.id);
  	console.log(modal)

  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

/*ajax*/

const form = document.getElementById('modal-form');
form.addEventListener("submit", submitHandler);

function submitHandler(e) {
    e.preventDefault();
    $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : 'modal_form', // the url where we want to POST
        data        : $('#modal-form').serialize(), // our form data
        dataType    : 'json', // what type of data do we expect back from the server
        success     : successFunction
    });
}

function successFunction(msg) {
    if (msg.message === 'success') {
         modal.style.display = 'none';
        form.reset()
    }
}


