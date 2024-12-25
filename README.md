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

- **YOLOv8**: Advanced real-time object detection for identifying key elements in the video.  
- **OpenCV**: A powerful library for image and video processing tasks.  
- **Python**: The primary language for implementing the analysis pipeline.  
- **NumPy**: For numerical operations and data handling.  

## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/sahilnayak7702/Football-Analysis-ComputerVision.git
   cd Football-Analysis-ComputerVision
