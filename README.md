# 🧵 Ring String Art Generator (Console Application)

This repository contains a Python-based console application designed to convert standard images into intricate circular "String Art." By simulating a continuous dark thread woven between discrete points (nails) placed on a circular ring, the algorithm procedurally recreates the original input image.

## 🚀 Project Overview
**Technologies:** `Python`, `OpenCV (cv2)`, `NumPy`

The core algorithm operates by analyzing the darkness of pixels along potential lines between nails. It selects the line that covers the darkest remaining pixels in the source image, virtually "draws" the string, and lightens that path on the reference image so the algorithm can iteratively seek out the next darkest path.

## 📂 Repository Structure

The project is divided into modular, object-oriented-like Python scripts, separating image processing, geometry, and algorithmic logic:

### `app.py`
The main execution script. It orchestrates the entire string art generation process, linking the image processing phase with the mathematical line-drawing algorithms. 

### `imageOperator.py`
Handles all computer vision and image preprocessing tasks. Utilizing OpenCV and NumPy, this module is responsible for loading the input image (e.g., `test.png`), resizing it, converting it to grayscale, and adjusting contrasts. This ensures the algorithmic logic has a clean, circular canvas to evaluate.

### `nailOperator.py`
Manages the geometry of the physical medium. This module calculates the exact Cartesian coordinates for a specified number of "nails" distributed evenly along the circumference of the circular canvas. It acts as the anchor point reference for all string connections.

### `lineOperator.py`
The mathematical core of the simulation. This script computes the pixel-perfect paths between any two nails (often utilizing concepts akin to Bresenham's line algorithm). It evaluates pixel intensities along these paths to help the main loop determine the most optimal next string connection.

---
