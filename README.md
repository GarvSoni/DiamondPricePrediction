## End to End ML Project

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
    (then goto browser and run http://<IP>:<port>/ and http://<IP>:<port>/predict for testing)
```
