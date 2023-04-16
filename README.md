## End to End Diamond Price Prediction ML Project

This project predicts the price of diamonds using linear regression. The pipeline includes exploratory data analysis, data preparation, model training, and prediction. The project is dockerized and deployed to the cloud with GitHub Actions for continuous integration and continuous deployment (CI/CD).

### Create an Environment 
```
    conda create -p diamondprice python==3.8    
```
### Activate the Environment 
```
    conda activate diamondprice/
```
### To install requirements 
```
    pip install -r requirements.txt
```
### To run this Project 
```
    python app.py
```
### If you want to build docker (OPTIONAL)
```
    docker build -t diamondprice:v1 .
    docker run --name=diamond --net=host -d -t diamondprice:v1
    (then goto browser and run http://<IP>:<port>/ for home page and http://<IP>:<port>/predict for testing the model.)
```
