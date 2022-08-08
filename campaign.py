from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'
app_secret = 'a81f13399cbc798e791d1dd4bb4fdaf4'
app_id = '381649527430463'
id = 'act_806311373713929'

FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
  'special_ad_categories': [],


}
print(AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)
)
