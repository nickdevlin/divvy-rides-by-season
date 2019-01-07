google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawAnnotations);

function drawAnnotations() {
      var data = google.visualization.arrayToDataTable([
        ['Day', 'Summer', 'Winter'],
        ['Sunday', 21.0, 10.5],
        ['Monday', 16.7, 12.7],
        ['Tuesday', 16.2, 11.2],
        ['Wednesday', 15.5, 10.3],
        ['Thursday', 15.0, 14.3],
        ['Friday', 16.4, 15.5],
        ['Saturday', 22.8, 13.4]
      ]);

      var data = google.visualization.arrayToDataTable([
        ['City', 'Summer', {type: 'string', role: 'annotation'},
         'Winter', {type: 'string', role: 'annotation'}],
        ['Sunday', 21.0, '21.0', 10.5, '10.5'],
        ['Monday', 16.7, '16.7', 12.7, '12.7'],
        ['Tuesday', 16.2, '16.2', 11.2, '11.2'],
        ['Wednesday', 15.5, '15.5', 10.3, '10.3'],
        ['Thursday', 15.0, '15.0', 14.3, '14.3'],
        ['Friday', 16.4, '16.4', 15.5, '15.5'],
        ['Saturday', 22.8, '22.8', 13.4, '13.4']
      ]);

      var options = {
        title: 'Average Length of a Bike Ride in Chicago',
        chartArea: {width: '60%'},
        height: 500,
        colors: ['#ff9223', '#66ccff'],
        annotations: {
          alwaysOutside: true,
          textStyle: {
            fontSize: 12,
            auraColor: 'none',
            color: '#555'
          },
          boxStyle: {
            stroke: '#ccc',
            strokeWidth: 1,
            gradient: {
              color1: '#f3e5f5',
              color2: '#f3e5f5',
              x1: '0%', y1: '0%',
              x2: '100%', y2: '100%'
            }
          }
        },
        hAxis: {
          title: 'Ride Length in Minutes',
          minValue: 0,
        },
        vAxis: {
          title: 'Day'
        }
      };
      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
