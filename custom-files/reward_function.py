def reward_function(params):
    '''
    Reward function to encourage speed and mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])
    speed = params['speed']

    # Calculate markers that are farther away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Reward based on distance from center
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/close to off track

    # Steering penalty threshold
    ABS_STEERING_THRESHOLD = 15

    # Penalize if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7

    # Significantly reward higher speeds
    SPEED_THRESHOLD = 3.0
    if speed > SPEED_THRESHOLD:
        reward *= 2.0

    return float(reward)
