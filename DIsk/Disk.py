from matplotlib import pyplot as plt
import os

class DiskScheduler:
    def __init__(self, initial_head_position, request_queue):
        self.initial_head_position = initial_head_position
        self.request_queue = request_queue

    def output(self, seek_operations, total_distance, seek_sequence):
        return seek_operations, total_distance, seek_sequence

    def fcfs(self):
        seek_sequence = [self.initial_head_position] + self.request_queue
        total_movement = abs(self.initial_head_position - self.request_queue[0])
        for i in range(1, len(self.request_queue)):
            total_movement += abs(self.request_queue[i] - self.request_queue[i-1])
        return self.output(len(seek_sequence), total_movement, seek_sequence)

    def sstf(self):
        request_queue = self.request_queue.copy()
        current_position = self.initial_head_position
        seek_sequence = [current_position]
        total_movement = 0

        while request_queue:
            next_request = min(request_queue, key=lambda x: abs(x - current_position))
            seek_sequence.append(next_request)
            total_movement += abs(next_request - current_position)
            current_position = next_request
            request_queue.remove(next_request)

        return self.output(len(seek_sequence), total_movement, seek_sequence)

    def scan(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            scan_sequence = left_requests[::-1] + [0] + right_requests
        else:
            scan_sequence = right_requests + [200] + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = self.initial_head_position
        for request in scan_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        return self.output(len(seek_sequence), total_movement, seek_sequence)

    def c_scan(self, direction):
        request_queue = sorted(self.request_queue)
        total_movement = 0
        seek_sequence = []

        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]

        if direction == "left":
            c_scan_sequence = left_requests[::-1] + [0] + [200] + right_requests[::-1]
        else:
            c_scan_sequence = right_requests + [200] + [0] + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = self.initial_head_position
        for request in c_scan_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        return self.output(len(seek_sequence), total_movement, seek_sequence)

    def look(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            look_sequence = left_requests[::-1] + right_requests
        else:
            look_sequence = right_requests + left_requests[::-1]

        seek_sequence.append(self.initial_head_position)
        previous = self.initial_head_position
        for request in look_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        return self.output(len(seek_sequence), total_movement, seek_sequence)

    def c_look(self, direction):
        request_queue = sorted(self.request_queue)
        left_requests = [req for req in request_queue if req < self.initial_head_position]
        right_requests = [req for req in request_queue if req >= self.initial_head_position]
        total_movement = 0
        seek_sequence = []

        if direction == "left":
            c_look_sequence = left_requests[::-1] + right_requests[::-1]
        else:
            c_look_sequence = right_requests + left_requests

        seek_sequence.append(self.initial_head_position)
        previous = self.initial_head_position
        for request in c_look_sequence:
            seek_sequence.append(request)
            total_movement += abs(request - previous)
            previous = request

        return self.output(len(seek_sequence), total_movement, seek_sequence)


def plot_seek_sequence(algorithm, seek_sequence, total_distance):
    plt.figure(figsize=(10, 6))
    plt.plot(seek_sequence, range(len(seek_sequence)), color="green", marker='o', markersize=5, linewidth=2)
    plt.title(f"{algorithm} Seek Sequence")
    plt.xlabel("Cylinder")
    plt.ylabel("Request")
    plt.text(172.5, -8.85, f"Total distance traveled: {total_distance} cylinders", horizontalalignment='center', verticalalignment='center', fontsize=12)

    # Annotate only the x-coordinate of each point with a slight offset
    for i, x in enumerate(seek_sequence):
        plt.text(x, i, f"{x}", fontsize=8, ha='left', va='center', rotation=0, color='blue', bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.2'))

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Save the image to the static folder
    image_path = os.path.join('static', f'{algorithm}_seek_sequence.png')
    plt.savefig(image_path)
    plt.close()
    
    return image_path



