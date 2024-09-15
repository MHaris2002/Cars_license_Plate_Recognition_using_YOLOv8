# Cars License Plate Recognition using YOLOv8
## Demo


https://github.com/user-attachments/assets/2495af25-6abe-46fc-861d-762e03bcc797



## Video Used

The video I used in this tutorial can be downloaded from [here](https://www.pexels.com/video/vehicles-traveling-on-daytime-8321860/).

## Model

The license plate detection model has been trained using the YOLOv8 framework for high-precision detection. 
- You can access the trained model [here](https://github.com/MHaris2002/Cars_license_Plate_Recognition/tree/main/model). 
-  The dataset used for training can be found [here](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

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
* Run main.py with the sample video file to generate new_test_alphabets,csv. Make few changes in functions.py and main.py as mentioned in code and re-run this command to generate new_test_numeric.csv.
``` python
python main.py
```
* Run Merge.py to merge both csv
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
