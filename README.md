# Cars License Plate Recognition using YOLOv8
## Demo


https://github.com/user-attachments/assets/9c0bf947-2614-444b-ab92-244485d0559b




## Description

This project involves the development of an AI-powered system designed for real-time vehicle detection, license plate recognition, and tracking from video footage. It utilizes a combination of state-of-the-art computer vision techniques and deep learning models for accurate identification and extraction of vehicle and license plate information.

The system integrates the following key components:

- **YOLOv8 Nano Model:** A lightweight deep learning model is used for real-time vehicle detection and license plate localization, ensuring fast processing on resource-limited hardware.
- **EasyOCR:** An OCR library that extracts license plate characters from the detected plates, facilitating license plate recognition.
- **SORT (Simple Online and Realtime Tracking):** A tracking algorithm used for associating detected objects (vehicles) across video frames to maintain consistent identification.
- **OpenCV:** Utilized for image preprocessing, manipulation, and post-processing tasks, such as drawing bounding boxes and applying visual enhancements.


## Video Used

The video I used in this project can be downloaded from [here](https://www.pexels.com/video/vehicles-traveling-on-daytime-8321860/).

## Model

The license plate detection model has been trained using the YOLOv8 framework for high-precision detection. 
- You can access the trained model [here](https://github.com/MHaris2002/Cars_license_Plate_Recognition/tree/main/model). 
- The dataset used for training can be found [here](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

## Dependencies

The sort module needs to be downloaded from [this repository](https://github.com/abewley/sort).

## Project Setup

* Make an environment with python ad clone this repository
``` bash
git clone https://github.com/MHaris2002/Cars_license_Plate_Recognition.git
```
* Navigate to project directory
``` bash
cd Cars_license_Plate_Recognition
``` 

* Install the project dependencies using the following command 
```bash
pip install -r requirements.txt
```
* Run main.py with the sample video file to generate new_test_alphabets.csv. Make few changes in functions.py and main.py as mentioned in code and re-run this command to generate new_test_numeric.csv.
``` python
python main.py
```
* Set the paths of both csv files and run Merge.py to merge both csv
``` python
python Merge.py
```
* Run the add_missing_data.py file for interpolation of values to match up for the missing frames and smooth output.
```python
python missing_frames.py
```

* Finally run the visualize.py passing in the interpolated csv files and hence obtaining a smooth output for license plate detection.
```python
python Visualization.py
```
