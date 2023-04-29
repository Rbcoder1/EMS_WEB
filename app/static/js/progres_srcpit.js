
var profile = document.getElementById("Profile");
var progress = document.getElementById("progress");
var job = document.getElementById("job");
var learning = document.getElementById("learning");
var recent = document.getElementById("recent");
var helproom = document.getElementById("helproom");



// progress section script 

const myChart = new Chart("myChart", {
    type: "line",
    data: {},
    options: {}
});

const xValues = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Agust", "Sep", "Oct", "Nov", "Dec"];
const yValues = [20, 04, 02, 12, 04, 00, 8, 00, 00, 00, 00, 10, 30]
new Chart("myChart", {
    type: "line",
    data: {
        labels: xValues,
        datasets: [{
            data: yValues,
            borderColor: "blue",
            fill: true
        }]
    },
    options: {
        legend: { display: false }
    }
});


var barColors = [
    "rgba(0,0,255,1.0)",
    "rgb(223, 68, 68)"
];

const xV = ["active", "not active"];
const yV = [10, 90]

new Chart("myDoughnut", {
    type: "doughnut",
    data: {
        labels: xV,
        datasets: [{
            backgroundColor: barColors,
            data: yV
        }]
    },
    options: {
        title: {
            display: false,
            text: "World Wide Wine Production"
        }
    }
});