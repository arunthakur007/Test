from flask import Flask,render_template
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
import requests

app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def crete_campaign():
    params = {
        'name': 'My campaign',
        'objective': 'LINK_CLICKS',
        'status': 'PAUSED',
        'special_ad_categories': [],
    }
    campaign_id = AdAccount(account_id).create_campaign(fields=fields,params=params)
    camp_id = campaign_id.get('id')
    return render_template('campaign.html',context=camp_id)


@app.route("/adset",methods=['GET','POST'])
def create_ad_set():
    print(requests.get,"===========================")
    params = {
        'name': 'Ad sets',
        'campaign_id': '120330000237404504',
        'daily_budget': '500000000',
        'start_time': '2021-08-05T11:39:08-0700',
        'end_time': '2022-08-12T11:39:08-0700',
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': 'REACH',
        'bid_amount': '1000',
        'promoted_object': {'page_id': page_id},
        'targeting': {'facebook_positions': ['feed'], 'geo_locations': {'countries': ['US']}},
        'user_os': 'iOS',
        'publisher_platforms': 'facebook',
        'device_platforms': 'mobile',
    }
    stores = (AdAccount(account_id).create_ad_set(fields=fields,params=params))
    get_adset_id = stores.get('id')
    return render_template('adset.html', context=get_adset_id)

@app.route("/adset/image")
def Create_image_hash():
    url = "https://graph.facebook.com/v14.0/" + str(account_id) + "/adimages"
    payload = {}
    files = [
        ('filename', ('test.jpg', open(path, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    image_hashes = eval(response.text).get('images').get('test.jpg').get('hash')
    context = {
        'c': image_hashes
    }
    print(image_hashes)

    return render_template('image_hash.html',context=context)


@app.route("/adset/image/adcreative",methods=['GET','POST'])
def create_ad_creative():
    print(requests.get, "===========================")
    params = {
        'name': 'Sample Creative',
        'object_story_spec': {'page_id': page_id,
                              'link_data': {'image_hash': image_hash,
                                            'link': 'https://www.facebook.com/Good-Times-104210345727280/',
                                            'message': 'try it out'}},
    }
    create_ad_creative_id = AdAccount(account_id).create_ad_creative(fields=fields, params=params)
    ad_create_id = create_ad_creative_id.get('id')


    return render_template('adcreative.html', context= ad_create_id)



@app.route("/adset/image/adcreative/adcreate",methods=['GET','POST'])
def create_ad():
    print(requests.get, "===========================")
    params = {
        'name': 'My Ad',
        'adset_id': adset_id,
        'creative': {'creative_id': creative_id},
        'status': 'PAUSED',
    }
    create_ad_id=AdAccount(account_id).create_ad(fields=fields,params=params)
    create_id=create_ad_id.get('id')
    # print(create_id)
    return render_template('adcreate.html', context=create_id)





if __name__ == '__main__':
    access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
    app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
    app_id = '381649527430463'
    account_id = 'act_806311373713929'
    path = 'test.jpg'
    page_id = '104210345727280'
    image_hash='349f13a614e0452ddceacfcc55877cb7'
    adset_id=120330000237475904
    creative_id=120330000237476804
    FacebookAdsApi.init(access_token=access_token)
    fields = []
    app.run()
