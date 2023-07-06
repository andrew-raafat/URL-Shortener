function myFunction() {
    var copyText = document.getElementById("myInput");
  
    copyText.select();
    copyText.setSelectionRange(0, 99999); 
  
    navigator.clipboard.writeText(copyText.value);
  
    alert("Copied the text: " + copyText.value);
  }

function myFunction2(i) {
  var copyText = document.getElementById(i);

  copyText.select();
  copyText.setSelectionRange(0, 99999); 

  navigator.clipboard.writeText(copyText.value);

  alert("Copied the text: " + copyText.value);
}