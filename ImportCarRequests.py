import requests

url = 'https://www.autotrader.com/rest/searchresults/base'

# This section represents the parametrization for the script
# TODO externalize the parameters

params = dict(
    zip=90210,
    makeCodeList='ROV',
    modelCodeList='DEFEND',
    marketExtension='true',
    maxMileage=150000,
    startYear=1980,
    endYear=2013,
    searchRadius=500,
    maxPrice=100000,
    sortBy='mileageASC',
    numRecords=100,
    firstRecord=0,
    style='Truck'
)

headers = {
    'Cache-Control': 'no-cache',
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

resp = requests.get(url=url, params=params, headers=headers)

data = resp.json()

hasnav = "false"

if 'listings' not in data:
    print('NO MATCH FOUND', end='\n\r')
else:
    for listing in data['listings']:

        print(str(listing['id']).expandtabs(16), end='\t')

        if ('features' in listing):
            for feature in listing['features']:
                if('nav' in feature.lower()):
                    hasnav = "true"
                    break

        if(hasnav == 'true'):
            print('NAV', end='\t')
        else:
            print('---', end='\t')

        if('mileage' in listing['specifications']):
            print(listing['specifications']['mileage']['value'].replace(',', ''), end=' ')
            if(listing['specifications']['mileage']['label'] != 'miles'):
                print("km".expandtabs(2), end='\t')
            else:
                print("mi".expandtabs(2), end='\t')
        else:
            print('----------$', end='\t')

        if('pricingDetail' in listing):
            if('incentive' in listing['pricingDetail']):
                print(str(listing['pricingDetail']['incentive']).expandtabs(12), end='')
                print('$'.expandtabs(6), end='\t')
            else:
                print(' '.expandtabs(6), end='\t')

        if(listing['priceValidUntil']):
            print(listing['priceValidUntil'], end='\t')

        if(listing['pricingDetail']):
            if(listing['pricingDetail']['salePrice']):
                print(str(listing['pricingDetail']['salePrice']).expandtabs(12), end='')
                print('$', end='\t')
            else:
                print('------$', end='\t')

        if('vin' in listing):
            print(listing['vin'].expandtabs(20), end='\n\r')
        else:
            print('-----------------', end='\n\r')


