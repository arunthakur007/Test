from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi


access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
app_id = '381649527430463'
id = 'act_806311373713929'


FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Ad',
  'adset_id': '120330000237123904',
  'creative': {'creative_id':'120330000237003104'},
  'status': 'PAUSED',
}
print(AdAccount(id).create_ad(
  fields=fields,
  params=params,
))

