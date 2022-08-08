import requests,json

ad_account_id ='act_806311373713929'

path = 'test.jpg'
access_token = 'EAAFbG7SC3T8BAAAEzmQOKRLatZAJEHHFCY1VgPZBJCjJBPrmZBAi83uFdFEsp4BRKqUaTkngZAYn5pbzi2qRiokptBZAqxmguTQUz96fZBGwF2ZBPOIn383emlaGGcWIcbygYHI8vkAeiRHZCxXSOq5wzfZAkQEoB2BcXE1zFLOLJM4ElCgp8ZCBDQMvkV201fff8ZD'

def Create_image_hash():
  url = "https://graph.facebook.com/v14.0/"+str(ad_account_id)+"/adimages"
  payload={}
  files=[
    ('filename',('test.jpg',open(path,'rb'),'image/jpeg'))
  ]
  headers = {
    'Authorization':  f'Bearer {access_token}',
  }
  response = requests.request("POST", url, headers=headers, data=payload, files=files)

  image_hashes = eval(response.text).get('images').get('test.jpg').get('hash')
  print(image_hashes)
  return image_hashes
Create_image_hash()






