from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
app_id = '381649527430463'
id = 'act_806311373713929'
page_id = '104210345727280'


FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Sample Creative',
  'object_story_spec': {'page_id':'104210345727280','link_data':{'image_hash':'349f13a614e0452ddceacfcc55877cb7','link':'https://www.facebook.com/Good-Times-104210345727280/','message':'try it out'}},
}
print (AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
))

