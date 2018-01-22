var data = new FormData();
alert("drin");
time = document.getElementsByClassName("time");

data.append('time', time);

var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://ec2-54-157-225-125.compute-1.amazonaws.com/twitter', true);
 function sendToServer() {
    // do something to response
    console.log(this.responseText);
};
xhr.send(data);