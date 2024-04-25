from flask import Flask, render_template, request
from Disk import DiskScheduler, plot_seek_sequence

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    initial_head_position = int(request.form['initial_head_position'])
    request_queue = list(map(int, request.form['request_queue'].split()))
    direction = request.form['direction'].lower()

    scheduler = DiskScheduler(initial_head_position, request_queue)

    results = {}
    results["FCFS"] = scheduler.fcfs()
    results["SSTF"] = scheduler.sstf()
    results["SCAN"] = scheduler.scan(direction)
    results["C-SCAN"] = scheduler.c_scan(direction)
    results["LOOK"] = scheduler.look(direction)
    results["C-LOOK"] = scheduler.c_look(direction)

    images = {}
    for algorithm, (seek_operations, total_distance, seek_sequence) in results.items():
        image_path = plot_seek_sequence(algorithm, seek_sequence, total_distance)
        images[algorithm] = image_path

    return render_template('result.html', results=results, images=images)

if __name__ == '__main__':
    app.run(debug=True)
    
