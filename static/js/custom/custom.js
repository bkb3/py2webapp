// Part of py2html package
// License GNU GLP v3 or later on your opinion
// author: github@bkb3

$(document).ready(function () {
    document.forms["input-form"].reset();
    $(
        ".floating-label .custom-select, .floating-label .form-control"
    ).floatinglabel();
    Waves.attach(".btn");
    Waves.init();
});

function afterSubmit() {
    $('#submit-btn').prop('disabled', true);
    $('#progress-console').collapse('toggle');
    $('#banner').collapse('hide');
    $('#pbar').css("width", "2%");
}


function success(data) {
    $('#console-body').append('<br><span class="text-monospace text-success">Data received!</span>');
    $('#pbar').text('Completed!');
    $('#pbar').attr('class', 'progress-bar bg-success');
    $('#pbar').css("width", "100%");
    setTimeout(function () {
        $('#progress-console').collapse('toggle');
        $('#results-page').collapse('toggle');
        // console.log('We received data from the backend');
        // console.log(data);
        showResults(data);
    }, 500);
}

function failure(data) {
    // console.log(data);
    // let msg = ''
    // if (data.status !== '500'){
    //     msg = data.statusText;
    // } else {
    //     msg = data['error'] === 'undefined' ? 'Unable to communicate with the backend.' : data['error']
    // }
    let msg = data['error'] === 'undefined' ? 'Unable to communicate with the backend.' : data['responseJSON']['error']
    // console.log(msg, data)
    $('#console-body').append('<br><span class="text-monospace text-danger">' + msg);
    $('#pbar').attr('class', 'progress-bar bg-danger');
    $('#pbar').css("width", "100%");
    $('#retry-btn-console').collapse('toggle');
}

function parseResults(json, status) {
    if (status != 'success') {
        failure(json, status)
    } else {
        success(json);
    }
}

function showResults(data) {
    $('#progress-console').collapse('toggle');
    $('#results-page').collapse('toggle');

    data.results.length ?
        $.each(JSON.parse(data.results.replace(/'/g, '"')), function (index, val) {
            if (index !== 'Plot') {
                $('#results-placeholder').append(`
                <p class="h3">${index}</p>
                <p>${val}</p>`
                )
            } else {
                $('#result_plot').css({
                    "position": "relative",
                    "margin": "auto",
                    "height": "40vh",
                    "width": "60vw"
                })
                $('#result_plot').append(
                    `<canvas id="newChart"></canvas>`
                )
                val.x.length ? plot(val) : null
            }
        }) : null;

    data.errors.length ? $('#results-placeholder-errors').append(
        `<p class="h3">Some errors occured</p> <p>${data.errors}</p>`
    ) : null;

}

function plot(data) {
    var ctx = document.getElementById('newChart').getContext('2d');
    let datasets = []

    $.each(data.y, function(index, item) {
        let tmp = {}
        tmp["label"]= data.ylabel[index],
        tmp["data"]=item,
        tmp["lineTension"]= 0.3,
        tmp["fill"] = false,
        tmp["borderCapStyle"]= "butt",
        tmp["borderDash"]= [],
        tmp["borderDashOffset"]= 0.0,
        tmp["borderJoinStyle"]= "miter",
        tmp["pointBorderWidth"]= 1,
        tmp["pointHoverRadius"]= 5,
        tmp["pointHoverBorderWidth"]= 2,
        tmp["pointHitRadius"]= 10,
        
        datasets.push(tmp)
    });

    new Chart(ctx, {
        type: !data.type ? 'line' : data.type,
        data: {
            labels: data.x,
            datasets: datasets,
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: data.xlabel
                    },
                }],
                // yAxes: [{
                //     display: true,
                //     scaleLabel: {
                //         display: true,
                //         labelString: data.ylabel
                //     },
                // }]
            },
            plugins: {
                colorschemes: {
                    scheme: 'brewer.SetOne3'
                }
            }
        }
    });
}
