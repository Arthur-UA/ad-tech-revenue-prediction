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
### Usage example
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
    "total_impressions": 46,
    "viewable_impressions": 28,
    "week_day": 3,
    "profitable_region": 1,
    "eCPM": 20,
    "uninformative_impressions": 0
}
```
Running api_usage.py give the following result:
```
0.7708225250244141
```
