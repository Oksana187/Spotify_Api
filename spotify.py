import requests
import base64

def get_artist_info(artist_name):
    '''
    Funcrion to get the artist name, the most popular song, and available markets.
>>> get_artist_info('ACDC')
{'artist_name': 'AC/DC', 'track_name': 'Highway to Hell', 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', \
'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', \
'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', \
'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', \
'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', \
'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', \
'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', \
'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', \
'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', \
'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', \
'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK']}
    '''
    CLIENT_ID = 'b2d4daf524d44f81a1d5902946f765ce'
    CLIENT_SECRET = '2390f673b70f4e398cbb41b716c4208e'

    auth_code = f'{CLIENT_ID}:{CLIENT_SECRET}'

    coded_credentials = base64.b64encode(auth_code.encode()).decode()
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {'grant_type': 'client_credentials'}
    auth_headers = {'Authorization': f'Basic {coded_credentials}'}
    response = requests.post(auth_url, data=auth_data, headers=auth_headers)
    access_token = response.json().get('access_token')
    base_url = 'https://api.spotify.com/v1/search/'

    request_params = {
        'query': artist_name,
        'type': 'artist'
    }

    request_headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(base_url, headers=request_headers, params=request_params)
    response_data = response.json()
    artist_id = response_data.get('artists').get('items')[0].get('id')
    top_tracks = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'

    top_tracks_params = {
        'country': 'US'
    }

    top_tracks_headers = {'Authorization': f'Bearer {access_token}'}
    top_tracks_response = requests.get(top_tracks, headers=top_tracks_headers, params=top_tracks_params)
    top_tracks_data = top_tracks_response.json()
    top_tracks = top_tracks_data.get('tracks')[0]
    track_id = top_tracks.get('id')
    track_info = f'https://api.spotify.com/v1/tracks/{track_id}'
    auth_headers = {'Authorization': f'Bearer {access_token}'}
    track_info_response = requests.get(track_info, headers=auth_headers)

    track_data = track_info_response.json()
    artist_name = track_data.get('artists')[0].get('name')
    track_name = track_data.get('name')
    available_markets = track_data.get('available_markets')

    return {'artist_name': artist_name, 'track_name': track_name, 'available_markets': available_markets}


# print(get_artist_info('ACDC'))

