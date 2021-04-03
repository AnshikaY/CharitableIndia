
// DONATE


function don_info(){
  var start = prompt("To proceed payment verify you are not a robot by completing the given CAPTCHA : 2ALV4");
  while(start != '2ALV4'){
    alert("Incorrect CAPTCHA")
    start = prompt("To proceed payment verify you are not a robot by completing the given CAPTCHA : 2ALV4");
  }
  alert("Donation Successful. Thank you!");
}