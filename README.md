## AdTech - Revenue prediction
### The idea of this project
The key idea of this project is to take an open source dataset from kaggle and build a model that will estimate the total ad company revenue based on some input data provided in order to know the Impact of Digital Advertisement for any Business.
Also it's important to cover the model as a REST API and predict the revenue with JSON input.
The dataset is available via the [link](https://www.kaggle.com/datasets/vaishnavkapil/adtech).
### The basic information about the dataset
The whole description of the data is provided on the official kaggle page, but there are some additional features that were created during the analysis provided in the python notebook.
These columns are:
- __Week day__: refers to a current week day.
- __Profitable region__: refers to a 181 region id which as it was discovered had the most revenue.
- __eCPM__: effective cost per mile, refers to a total revenue per thousand impressions with respect to site and ad unit ids.
- __Uninformative impressions__: refers to a difference between viewable and measurable impressions.
### Prerequisites
It's important to have the python 3.9+.
You have to run the following command in your terminal to install all required packages:
```
pip install -r requirements.txt
```
### Usage example (with python script)
First you have to run app.py to start the locahost.
Then you have to prepare the input.json file with your own data.
The example of input.json file that can be used for providing the input data to the model:
```
{
    "site_id": 350,
    "ad_type_id": 10,
    "device_category_id": 1,
    "advertiser_id": 79,
    "order_id": 3485,
    "line_item_type_id": 8,
    "os_id": 56,
    "monetization_channel_id": 19,
    "ad_unit_id": 5168,
    "total_impressions": 4600,
    "viewable_impressions": 2008,
    "week_day": 3,
    "profitable_region": 1,
    "eCPM": 30,
    "uninformative_impressions": 0
}
```
Running api_usage.py will send a request to the localhost and get the following prediction:
```
{
  "total_revenue": 31.516813278198242
}
```
### Usage example (with cURL)
First you have to run app.py to start the localhost.
Then you can the use the following curl example to send a request:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "site_id": 350,
    "ad_type_id": 10,
    "device_category_id": 1,
    "advertiser_id": 79,
    "order_id": 3485,
    "line_item_type_id": 8,
    "os_id": 56,
    "monetization_channel_id": 19,
    "ad_unit_id": 5168,
    "total_impressions": 0,
    "viewable_impressions": 0,
    "week_day": 6,
    "profitable_region": 0,
    "eCPM": 0,
    "uninformative_impressions": 0
}'
```
And get the following result:
```
{
  "total_revenue": 0.004325652029365301
}
```
