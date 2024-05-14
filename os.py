import random

def fcfs(initial_position, requests):
    total_head_movements = 0
    current_position = initial_position
    
    # Iterate over the requests
    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    
    return total_head_movements

def scan(initial_position, requests, start_from_left=True):
    total_head_movements = 0
    current_position = initial_position
    
    # Find index of current position in requests
    index = requests.index(current_position)
    
    # Determine the range for scanning based on the direction
    if start_from_left:
        range_start = index
        range_end = len(requests)
    else:
        range_start = index - 1
        range_end = -1
    
    # Move towards the end or beginning based on the direction
    for i in range(range_start, range_end, -1 if start_from_left else 1):
        total_head_movements += abs(requests[i] - current_position)
        current_position = requests[i]
    
    # Move towards the opposite direction
    opposite_direction = not start_from_left
    range_start = 0 if opposite_direction else len(requests) - 1
    range_end = index + 1 if opposite_direction else -1
    
    for i in range(range_start, range_end, 1 if opposite_direction else -1):
        total_head_movements += abs(requests[i] - current_position)
        current_position = requests[i]
    
    return total_head_movements

def c_scan(initial_position, requests, start_from_left=True):
    total_head_movements = 0
    current_position = initial_position
    
    # Determine the range for scanning based on the direction
    if start_from_left:
        scan_range = range(current_position, 5000)
    else:
        scan_range = range(current_position, -1, -1)
    
    # Move towards the end or beginning based on the direction
    for request in scan_range:
        if request in requests:
            total_head_movements += abs(request - current_position)
            current_position = request
    
    # Move to cylinder 0
    total_head_movements += current_position
    current_position = 0
    
    # Move towards the opposite direction
    opposite_direction = not start_from_left
    if opposite_direction:
        scan_range = range(4999, -1, -1)
    else:
        scan_range = range(5000)
    
    for request in scan_range:
        if request in requests:
            total_head_movements += abs(request - current_position)
            current_position = request
    
    return total_head_movements


def main(file_path='numbers.txt'):  # Default value for file_path
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    
    initial_position = random.choice(requests)  # Randomly select initial position
    print("Initial Position:", initial_position)
    
    direction_input = input("Start scanning from left for SCAN? (Y/N): ").upper()
    start_from_left = direction_input == 'Y'
    
    direction_input = input("Start scanning from left for C-SCAN? (Y/N): ").upper()
    start_from_left_C = direction_input == 'Y'

    fcfs_head_movements = fcfs(initial_position, requests)
    scan_head_movements = scan(initial_position, requests, start_from_left)
    c_scan_head_movements = c_scan(initial_position, requests, start_from_left_C)
    
    print("Task 1 - FCFS Total Head Movements:", fcfs_head_movements)

    print("Task 1 - SCAN Total Head Movements:", scan_head_movements)

    print("Task 1 - C-SCAN Total Head Movements:", c_scan_head_movements)

    sorted_requests = sorted(requests)  
    
    fcfs_head_movements_task2 = fcfs(initial_position, sorted_requests)
    scan_head_movements_task2 = scan(initial_position, sorted_requests, start_from_left)
    c_scan_head_movements_task2 = c_scan(initial_position, sorted_requests, start_from_left_C)
    
    print("Task 2 - FCFS Total Head Movements:", fcfs_head_movements_task2)
    print("Task 2 - SCAN Total Head Movements:", scan_head_movements_task2)
    print("Task 2 - C-SCAN Total Head Movements:", c_scan_head_movements_task2)

if __name__ == "__main__":
    main()
