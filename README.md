# Football Analysis Using Computer Vision

## Overview

This project is a comprehensive analysis tool for football matches using state-of-the-art computer vision techniques. It processes match videos to detect players, referees, and the ball, tracks their movements, and provides insightful metrics like speed, distance covered, and team classifications. Built using the YOLOv8 object detection model and other advanced image processing techniques, this tool is designed to deliver real-time and precise analysis.

## Features

1. **Player and Referee Detection**  
   Accurately detects all players, referees, and the ball in the video frames using YOLOv8.  

2. **Ball Tracking**  
   Tracks the ball’s trajectory throughout the match for analysis of play patterns.  

3. **Team Classification**  
   Differentiates players into teams based on their uniform colors using color segmentation.  

4. **Speed and Distance Estimation**  
   Calculates the speed of players and the ball, along with the total distance covered.  

5. **Camera Motion Adjustment**  
   Compensates for moving cameras to ensure accurate tracking and spatial consistency.  

6. **Perspective Transformation**  
   Aligns the field’s perspective for consistent analysis regardless of camera angles.  

## Technologies Used

- **YOLO**: AI object detection model
- **Kmeans**: Pixel segmentation and clustering to detect t-shirt color
- **Optical Flow**: Measure camera movement
- **Perspective Transformation**: Represent scene depth and perspective
- Speed and distance calculation per player

## Installation and Setup

Take the following steps:  
   ```bash
   git clone https://github.com/sahilnayak7702/Football-Analysis-ComputerVision.git
   cd Football-Analysis-ComputerVision
   pip install -r requirements.txt
   # Place your football match video in the input_videos/ directory.
   python main.py --input input_videos/match.mp4 --output output_videos/analysis.mp4
   ```

## Key Concepts and Techniques
1. **Object Detection**: YOLOv8 identifies and locates players, referees, and the ball in each frame.

2. **Color Segmentation**:Differentiates team players by analyzing uniform colors.
   
3. **Kalman Filtering**:Smoothens object tracking by predicting positions in subsequent frames.


4. **Perspective Transformation**: This method maps the video feed to a consistent top-down view of the football field for accurate analysis.

5. **Video Processing**: Analyzes each frame in the video to seamlessly overlay detection and tracking information.



