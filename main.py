from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
app_id = '381649527430463'
id = 'act_806311373713929'
page_id = '104210345727280'

FacebookAdsApi.init(access_token=access_token)

fields=[]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
  'special_ad_categories': [],
  'name1': 'Ad sets',
  'campaign_id': 120330000237121504,
  'daily_budget': '500000000',
  'start_time': '2021-08-05T11:39:08-0700',
  'end_time': '2022-08-12T11:39:08-0700',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'REACH',
  'bid_amount': '1000',
  'promoted_object': {'page_id': 104210345727280},
  'targeting': {'facebook_positions': ['feed'], 'geo_locations': {'countries': ['US']}},
  'user_os': 'iOS',
  'publisher_platforms': 'facebook',
  'device_platforms': 'mobile',
  'name2': 'Sample Creative',
  'object_story_spec': {'page_id':'104210345727280','link_data':{'image_hash':'349f13a614e0452ddceacfcc55877cb7','link':'https://www.facebook.com/Good-Times-104210345727280/','message':'try it out'}},
  'name4': 'My Ad',
  'adset_id': '120330000237123904',
  'creative': {'creative_id':'120330000237003104'},
  'status1': 'PAUSED',
}



stores = (AdAccount('act_806311373713929').create_ad_set(
  fields=fields,
  params=params,
))


ad_set_id = stores.get_id()
print('ad_set_id:', ad_set_id, '\n')


print (AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
))


print(AdAccount(id).create_ad(
  fields=fields,
  params=params,
))
