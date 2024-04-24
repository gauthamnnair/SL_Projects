from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_light_color():
    # Generate random RGB values in the range [180, 255]
    r = random.randint(180, 255)
    g = random.randint(180, 255)
    b = random.randint(180, 255)
    # Format the RGB values as a hexadecimal color code
    return f"#{r:02X}{g:02X}{b:02X}"

def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    allocation_info = []
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                memory_wastage = blockSize[j]
                allocation_info.append((i + 1, processSize[i], j + 1, memory_wastage))
                break
            elif j == m - 1:
                allocation_info.append((i + 1, processSize[i], "Not Allocated", "-"))
    return allocation_info

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    allocation_info = []
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]
            memory_wastage = blockSize[bestIdx]
            allocation_info.append((i + 1, processSize[i], bestIdx + 1, memory_wastage))
        else:
            allocation_info.append((i + 1, processSize[i], "Not Allocated", "-"))
    return allocation_info

def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    allocation_info = []
    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1 or blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]
            memory_wastage = blockSize[wstIdx]
            allocation_info.append((i + 1, processSize[i], wstIdx + 1, memory_wastage))
        else:
            allocation_info.append((i + 1, processSize[i], "Not Allocated", "-"))
    return allocation_info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allocate', methods=['POST'])
def allocate():
    block_sizes = list(map(int, request.form['block_sizes'].split()))
    process_sizes = list(map(int, request.form['process_sizes'].split()))
    algorithm = request.form['algorithm']

    if algorithm == "First Fit":
        allocation_info = firstFit(block_sizes[:], len(block_sizes), process_sizes[:], len(process_sizes))
    elif algorithm == "Best Fit":
        allocation_info = bestFit(block_sizes[:], len(block_sizes), process_sizes[:], len(process_sizes))
    elif algorithm == "Worst Fit":
        allocation_info = worstFit(block_sizes[:], len(block_sizes), process_sizes[:], len(process_sizes))

    # Generate block colors
    block_colors = [generate_light_color() for _ in range(len(block_sizes))]

    return render_template('result.html', allocation_info=allocation_info, block_sizes=block_sizes, block_colors=block_colors)

if __name__ == '__main__':
    app.run(debug=True)

