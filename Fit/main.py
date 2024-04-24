from flask import Flask, render_template, request
import random

app = Flask(__name__)

def firstFit(blockSize, m, processSize, n):
    # Your existing firstFit function implementation

def bestFit(blockSize, m, processSize, n):
    # Your existing bestFit function implementation

def worstFit(blockSize, m, processSize, n):
    # Your existing worstFit function implementation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allocate', methods=['POST'])
def allocate():
    block_sizes = list(map(int, request.form['block_sizes'].split()))
    process_sizes = list(map(int, request.form['process_sizes'].split()))
    algorithm = request.form['algorithm']

    if algorithm == "First Fit":
        allocation, memory_usage = firstFit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))
    elif algorithm == "Best Fit":
        allocation, memory_usage = bestFit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))
    elif algorithm == "Worst Fit":
        allocation, memory_usage = worstFit(block_sizes, len(block_sizes), process_sizes, len(process_sizes))

    return render_template('result.html', block_sizes=block_sizes, memory_usage=memory_usage, allocation=allocation)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)

