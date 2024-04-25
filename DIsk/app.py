from flask import Flask, render_template, request
from matplotlib import pyplot as plt
from Disk import DiskScheduler, plot_seek_sequence

app = Flask(__name__,template_folder='templates')

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

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)

