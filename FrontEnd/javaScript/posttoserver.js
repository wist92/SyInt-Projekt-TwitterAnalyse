var data = new FormData();
time = document.getElementsByClassName("time");

data.append('time', time);

var xhr = new XMLHttpRequest();
xhr.open('POST', 'somewhere', true);
 function sendToServer() {
    // do something to response
    console.log(this.responseText);
};
xhr.send(data);