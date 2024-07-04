def reward_function(params):
    '''
    Reward function to encourage speed and mitigate going off track during turns
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']

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

    # Penalize if not all wheels are on track
    if not all_wheels_on_track:
        reward *= 0.1

    # Steering penalty threshold
    ABS_STEERING_THRESHOLD = 15

    # Penalize if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7

    # Reward higher speeds more significantly
    SPEED_THRESHOLD = 2.5
    if speed > SPEED_THRESHOLD:
        reward *= 1.5

    # Additional reward for completing the lap faster
    if progress == 100:
        reward += 10.0  # Large reward for completing the lap

    return float(reward)
