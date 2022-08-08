from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
app_id = '381649527430463'
id = 'act_806311373713929'
page_id = '104210345727280'

# access_token = 'EAARA6rESSMwBAPoPXhOMpRRM7K0xZCQYYok97S6XZACS9M45avn718VEOWp9sKSZA7yIf1d0ZCuysjRKZCEYSQZC8F1DToVdcPhgp5XUDnG9o2wZCgqySxZBGbxaR8WOiswjCtqlhZB6glbZCWlaMXc4bTpXrt5ZCeOMAoZBnepZCkM8YNrZAtZCA4j4KrCjkFhZCP38ZC1kZD'
# id = 'act_643750543324964'
# app_secret = '63415d2640298f6360fc63955a7e4d1b'
# app_id = '1197276644133068'
# page_id = '108929148277930'

FacebookAdsApi.init(access_token=access_token)
fields=[]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
  'special_ad_categories': [],
}



store = AdAccount('act_806311373713929').create_campaign(
  fields=fields,
  params=params,
)
# print(store)
campaign_id = store.get_id()
# print(campaign_id)


fields = [
]
params = {
  'name': 'Ad sets',
  'campaign_id': 120330000237159104,
  'daily_budget': '500000000',
  'start_time': '2021-08-05T11:39:08-0700',
  'end_time': '2022-08-12T11:39:08-0700',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'REACH',
  'bid_amount': '1000',
  'promoted_object': {'page_id':104210345727280},
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US']}},
  'user_os': 'iOS',
  'publisher_platforms': 'facebook',
  'device_platforms': 'mobile',
}
stores = (AdAccount('act_806311373713929').create_ad_set(
  fields=fields,
  params=params,
))
# print(stores)
ad_set_id = stores.get_id()
print('ad_set_id:', ad_set_id, '\n')