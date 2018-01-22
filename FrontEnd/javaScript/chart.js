function HichartStad(){
    var dataObject ;
    var nameland = [];
    var valeurhastag = [];
    const req = new XMLHttpRequest();
        req.onreadystatechange = function(event) {
            if (this.readyState === XMLHttpRequest.DONE) {
                if (this.status === 200) {
                    dataObject = JSON.parse(this.responseText);
                    for (var i = 0; i < dataObject.length; i++) {
                        name = JSON.stringify(dataObject[i]['full_name']);
                        name = name.replace(/"/g,'');
                         nameland.push(name);
                         valeurhastag.push(parseFloat(JSON.stringify(dataObject[i]['ftCount'])));
                     }
                     chartload(nameland,valeurhastag);
                    console.log(nameland);
                    console.log(valeurhastag);

                } else {
                    console.log("Status de la réponse: %d (%s)", this.status, this.statusText);
                }
            }


        };

        req.open('GET', 'https://1ethmtokja.execute-api.us-west-2.amazonaws.com/ApiLocation', true);
        req.send(null);

    function chartload(land,valeu) {
              var canvas = document.getElementById('barChart');
        var ctxB = canvas.getContext('2d');
        var myBarChart = new Chart(ctxB, {
              type: 'bar',
              data: {
                //labels: ["Berlin", "Paris", "NewYork", "Yaounde", "Syngapur", "Changai"],
                  labels: land,
                datasets: [{
                    label: 'Ursprungliche Länder',
                    //data: [500, 700, 250, 100, 50, 96],
                    data: valeu,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                borderWidth: 1
                }]
              },
              optionss: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
              }

        });

    }
    }
