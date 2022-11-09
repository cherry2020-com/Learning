var data = null;
var XMLHttpRequest = require('xhr2');
var xhr = new XMLHttpRequest();
xhr.withCredentials = false;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

//setting request method
//API endpoint for API sandbox 
xhr.open("GET", "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata4/sap/api_bank/srvd_a2x/sap/bank/0002/Bank?%24top=50");


//adding request headers
//API Key for API Sandbox
xhr.setRequestHeader("APIKey", "uKWGagvUkYWAli9AAAsuYekjuLAtocFk");
xhr.setRequestHeader("DataServiceVersion", "2.0");
xhr.setRequestHeader("Accept", "application/json");


//sending request
console.log(xhr.send(data));