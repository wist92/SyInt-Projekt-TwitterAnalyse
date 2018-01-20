alert("gut");
function test(){
         const req = new XMLHttpRequest();

        req.onreadystatechange = function(event) {
            // XMLHttpRequest.DONE === 4
            //this.responseType = 'json';
            if (this.readyState === XMLHttpRequest.DONE) {
                if (this.status === 200) {
                     console.log("Réponse reçue: %s",this.responseText);
                } else {
                    console.log("Status de la réponse: %d (%s)", this.status, this.statusText);
                }
            }
        };

        req.open('GET', 'https://1ethmtokja.execute-api.us-west-2.amazonaws.com/ApiLocation', true);
        req.send(null);


       }

function Hichart(){        
        var canvas = document.getElementById('barChart');
        var ctxB = canvas.getContext('2d');
        var myBarChart = new Chart(ctxB, {
              type: 'bar',
              data: {
                labels: ["Berlin", "Paris", "NewYork", "Yaounde", "Syngapur", "Changai"],
                datasets: [{
                    label: 'Kurve',
                    data: [500, 700, 250, 100, 50, 96],
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
      test();
    }
