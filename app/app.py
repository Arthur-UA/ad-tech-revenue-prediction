'''Creating a REST API to use the model for making predictions'''

import uvicorn
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
with open('model.pkl', 'rb') as f:
    model = joblib.load(f)

class AddCompany(BaseModel):
    '''Base class for providing the data to API'''
    site_id: int
    ad_type_id: int
    device_category_id: int
    advertiser_id: int
    order_id: int
    line_item_type_id: int
    os_id: int
    monetization_channel_id: int
    ad_unit_id: int
    total_impressions: int
    viewable_impressions: int
    week_day: int
    profitable_region: int
    eCPM: float
    uninformative_impressions: int

@app.post('/predict')
def predict(add_company: AddCompany):
    '''Predicting the total revenue based on the data from json'''
    data = add_company.dict()
    prediction = model.predict([
        [
            data['site_id'], data['ad_type_id'],
            data['device_category_id'], data['advertiser_id'],
            data['order_id'], data['line_item_type_id'],
            data['os_id'], data['monetization_channel_id'],
            data['ad_unit_id'], data['total_impressions'],
            data['viewable_impressions'], data['week_day'],
            data['profitable_region'], data['eCPM'], data['uninformative_impressions']
        ]
    ])

    return {'total_revenue': prediction.tolist()[0]}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
