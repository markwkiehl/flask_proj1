function getChartData() {
    $("#loadingMessage").html('<img src="/static/img/loading.gif" alt="" srcset="">');
    $.ajax({
        url: "http://127.0.0.1:5000/chart-handler",
        success: function (result) {
            $("#loadingMessage").html("");
            var data = [];
            data.push(result.thisWeek);
            var labels = result.labels;
            renderChart(data, labels);
        },
        error: function (err) {
            $("#loadingMessage").html("Error");
        }
    });
}

// event listener
document.addEventListener('DOMContentLoaded', function() {
    getChartData();
}, false);
