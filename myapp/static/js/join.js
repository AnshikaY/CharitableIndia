


// JOIN


function join_info(){
  var start = prompt("To submit the application verify you are not a robot by completing the given CAPTCHA : 1A4S3");
  while(start != '1A4S3'){
    alert("Incorrect CAPTCHA")
    start = prompt("To submit the application verify you are not a robot by completing the given CAPTCHA : 1A4S3");
  }
  alert("Application received. Further details will be mailed to you soon!");
}