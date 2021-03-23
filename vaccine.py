import os
import requests

cookies = {
    'bm_sz': '9DC9DE5A5082E4476CB2D8E7E9723861~YAAQFzPFF0uRTRp4AQAAyRzPOQs0cWvd63OihxY68JiSSFeC1+kBWwxv8O0f7G8+b3RSSBlsIDaCjk0IcAtkme2wh1p8Bc07CDFfj/oKS0IGQQxuJSjmGj22JlF6oKZ0UGAFG4P/RULc3DB3y8WPPtXiw3p8mifFzU83ftJDOH8E7krqFSUMRC96jF+cJzkW5q1G',
    'rxVisitor': '161587757881386K3A1P6LKO0R39NKRPTKEUO29E8S8PK',
    'wag_sid': 'jqqqaongybf8gmd70c6walca',
    'uts': '1615877580070',
    'ak_bmsc': 'DF71BDD8BE9D679EA8B7FFB2E78A334C17C533173A050000CA555060CF372C68~plf//6+SU9WGuTeptZnozFDpw5VztPjaXvHr4EK5Ey9QfWWXVnRBBCqDLhb6rgUlkkvNQM9vwhlcheYO3Fz3boohRLyqsesmOdIbSFWQesKLqiUZfnr03L2UkO2bAzjLcxUQeXjLYSQLQLxwWEPT83z6saa44UjnMVpi1FdFUJP+bhv+oWNK0oJYHAiBTN2RwBiZVxps3xAuqjkoBNkkJc5azz12JmBHivKs5rTOLdTg3JgIUmJSq05mfb3bxtLuF4',
    'fc_vnum': '1',
    'fc_vexp': 'true',
    '_gcl_au': '1.1.123430466.1615877582',
    'AMCVS_5E16123F5245B2970A490D45%40AdobeOrg': '1',
    'AMCV_5E16123F5245B2970A490D45%40AdobeOrg': '-1124106680%7CMCIDTS%7C18703%7CMCMID%7C54576486868720619713566018969118578078%7CMCAAMLH-1616482381%7C9%7CMCAAMB-1616482381%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615884781s%7CNONE%7CvVersion%7C5.2.0',
    'gpv_Page': 'https%3A%2F%2Fwww.walgreens.com%2Ffindcare%2Fvaccination%2Fcovid-19',
    's_cc': 'true',
    'session_id': '349fe0b4-750b-4c84-8996-5d478dd452e4',
    'dtCookie': f"2BBB2A9OKTVRPF5BJHTRRMGALBDSAUEPC|0eed2717dafcc06d|1",
    'gRxAlDis': 'N',
    'XSRF-TOKEN': 'DxUO2PjKKICTKA==.qfmjSnufN+Pfi9ujUB6aSZ9gvtk+1zbcMNUE9bmtC3o=',
    'USER_LOC': '2%2BsKJSc9HtK0OKdV8%2Be6tTufCKUgUi6A%2BRJd8%2BMJ70JBfBetdGRYxnQQ%2BK7rxsqc',
    's_sq': 'walgrns%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526link%253DSchedule%252520new%252520appointment%2526region%253DuserOptionButtons%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.walgreens.com%25252Ffindcare%25252Fvaccination%25252Fcovid-19%25252Flocation-screening%2526ot%253DA',
    'dtSa': '-',
    'dtLatC': '2',
    'rxvt': '1615880375378|1615877578814',
    'dtPC': f"278573535_361h-vBVRLGJHRFWPMPOJDODMAAQPKLEFWNFLR-0e17",
    '_abck': 'DEB2DAD152687BEF8C60B141BD455C48~0~YAAQBjPFFxbqVzl4AQAA72HeOQXf20IQC4HYzgMmr0yzwG8AI45pe+1g8sM8+MiF0UsnGwNLjVhGGrGysNXvnpY2rWkpVf7YVEz92RG51qiblGxk0UhqHA4GfjhTOxiAUB99vGrPe5AU0aZjBrEiouvgzrle78Dj1TpAX7SI30fyX7aNXYqbBE7YD17dDV+KEHIT5VBpbyrTtPDFn4k1j0c+Sn4CHPjDq21WWpT4R/SlqZYcGZbGClJTBIiqcydg9uSfnXvfnnt1Q8ydRdztc5Bi4IHG7i+F1NUt6KhAPBn7hKU/8fMmiji+KWLqwzfNrJrKzx+RCJHzwhAIfg7gKrFLoC6RVXQSzbzmqRKGy4IPyYzjVZXN+AKiy9BwWH0qZ6insnGrfN00YrEJ5+bN9vQegb0niXK2QSp7~-1~-1~-1',
    'akavpau_walgreens': '1615878880~id=7eb203ef4419c08a0c44c1c1d6db085c',
    'bm_sv': 'F09057B4E85347B8CC0290F5362B9C2C~/GGZEY2xMC/T1sImyY88nvxRP78z5Qkto2IoFPJu30ZOuTycxBB6PM7EZRIfOayaw+zPak008hQSC63yei54/mfA7+37i/caKgyKiv34JkFXA9pVVE3cJS4t/jh2FEmMzV3ry2RHPJe8SdfOyP0yyHpL9aH/u+ZK6jdaA3BHRFk=',
}

headers = {
    'authority': 'www.walgreens.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'x-xsrf-token': 'eSNqcz5X8Y0Yhg==.pBWCd7h2z3YHoGDBNTw1MNj0+QQOdmW9gpEbwTwMzIk=',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.walgreens.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
}


cookies2 = {
    'bm_sz': 'E6148767EAF0A88500B50E5385274F1E~YAAQDTPFF8mSJBx4AQAAjzTuPwvOim25XFo84LC93W4IQwQLniLP5rbAnqoZfM/jpsVUxaFQKAzjjhgikSKhWv4dsDSjJjVJ08Nbvp8c92BuQ1VI17KmAfbKGFiLW1sDxnJiw18l0GEsu/moL/ZN98uwsbFvTS/+T1NnfSUPkyDA4D/uhRWhLJXVkxkiX9fUzA1i',
    'XSRF-TOKEN': '9EePc1/fSK8oiA==.9kUO8gap0/dWJ2DVys/MnKBG43AQZH7CGqE8l22Of6Q=',
    'session_id': 'd2204bf1-0445-4d5c-af69-9d9f5f054377',
    'dtCookie': f"5EE4E78E9B224EDE2648247C8BE5EB04F|0eed2717dafcc06d|1",
    'mt.sc': '%7B%22i%22%3A1615980281442%2C%22d%22%3A%5B%5D%7D',
    'mt.v': '2.115777078.1615980281443',
    'at_check': 'true',
    '_gcl_au': '1.1.436481235.1615980282',
    'AMCVS_5E16123F5245B2970A490D45%40AdobeOrg': '1',
    's_cc': 'true',
    'rxVisitor': '161587757881386K3A1P6LKO0R39NKRPTKEUO29E8S8PK',
    'mt.mbsh': '%7B%22fs%22%3A1615980282119%7D',
    '3s': 'xJfEq8SeecSyw6DDkMWLWirDhz0=',
    'profileId': '200017957181',
    'FirstName': 'Sabrina',
    '2fa': '38ec36b8d4320c0ea4a7000b0a1d8a09',
    'bm_mi': 'D03C5129D612C94104D49E216F4C6F5D~6NzGY4ggzXJaP3Sct+KS0vlq7SPwGB/MewQFUYMHfpKokKaPtu2v6cCanBRY7zhwfhaBkP61hYkJ01My98fuoZr0R94JNqsEDKOrYR1FM3/m8koLjPYyb8Os2ALZ9uyCOYE9DpCdCf9M9d7L1Vvd0lfL9Q3fuhpE1s1CZvslKV2mmzhsjorZxlWiZZrB2o1dRISM5305ehVFKituZ/+QvyB4daodyS+3Cy/ebFNRscf4cx1KXJWGYHSJA/Qtqw8X1EOqveNmaRcDS4DPxyy0TzP7PnxRR/zV/16dOaQocw5kFEfr5sQS+wyLi1GtyrQ7cmDaa0u1fvneGOKKD3Iquw==',
    'wag_sid': 'm3iij6mnxdlhv613e50tdvt4',
    'uts': '1615980290030',
    'AMCV_5E16123F5245B2970A490D45%40AdobeOrg': '-1124106680%7CMCIDTS%7C18704%7CMCMID%7C54576486868720619713566018969118578078%7CMCAAMLH-1616585090%7C9%7CMCAAMB-1616585090%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615987490s%7CNONE%7CvVersion%7C5.2.0%7CMCCIDH%7C1611675534',
    'mbox': 'session#f05e853b64b34b938356ad727a692951#1615982142|PC#f05e853b64b34b938356ad727a692951.35_0#1679225091',
    'nsl': '1',
    'p_s': '1',
    '_4c_': '%7B%22_4c_s_%22%3A%22jVNdb6MwEPwrJ6TrUwHbgIFIUZWmrdTTNWnTqn1EfGyCW8DINiG5Kv%2F97CRtuJ50OnjAOzszrO3dd6svobFGmOIgjhCJqV6dW2%2Bwldbo3RKsMJ%2B1NbKiOECExsjOfMhsv4iJHSEI7DwP8iilcRijwjq3NsaLeGFASYw9n%2BzOrbw9erxbOS9Ae%2BHYwb7j2UupFeqXRmyfIL1uBS%2B6XCVq2xpeD9k3WbzpRAFrlkPSs0KVOkGQH53QEtiqVMYXB8TArTCBQwId9KwpeP%2BpxDQmJ%2FSkRL6BM8F7CUY9LQWv4VsUa5Trs7Be9gpTsIAlCLFnlUq1cuS6fd87fVqtBEAjnZzXbsVXrHFeZXshuvF3crPlnUjznHeN0lEBy7SrlMlrQ8nUfrdDgyOsL2KY0ej87mmRXF5PpvPZoABZgxIsl1%2BqyFwp3T3USBe7Px5t4hDiIPsqfJi5MqShhwlFkR95AbqYPFyO8VnNinHgByH1I6rfkCCK4xB7AaUIRzGNMY6CMEJhdDZ5uB5jXdPkMlEgzTmeAnKI%2BnSVSNNFVu0x9krrZlNU5ZpiDwKkirXyNamBvi254po1M10wWOdVKiXLh9C9YDU8lSDSFjqlN63xm7SSoHPPTJ%2FaC8BbtZ0UR%2F4em%2FKu5Y0cWtylrEoeH%2BcD%2BWLzxBegdOLAn%2FJmyUSdKsab%2B3Rlbml5pP7kqxUUyW1z2OcxnHfqa5x4ojhgi83Q%2B4Dd6LaapgJmvD%2FWdr0GseUNTE2vfBQsHXhOBdYdvVdlTORlxjdJBmmntokseXtkfqbaVKgGhCzZR6o1c4w%2Feuhuenul4%2F%2B7amt3HG1MEaV6hjw%2F1qOrKmsUUR%2BZZ3f4wX7S8Z9s7Yj%2BZh%2BGzYbmHzLyVbbb%2FQY%3D%22%7D',
    'bm_sv': '590C57F2DDC242F34475E6B358246F51~IUcSF5L0KQqMYx9DyOfVkKoYnc2D6QDa/yim71khZXhCQLvMlLCh0P/lG8m2oRQxzD8+s6GJILPJwkKkDlf1qWgM5Qu/aXUN74L5cG9veIs71YDR1ua2msqrFdI8YxILxUu+AZ2s0WILBqsT+5Yi+qjMKAEMX8Lc0MM87GRtR6I=',
    'ak_bmsc': '96BB68B1748AA180F78C93F5E64D949917C5330D520D0000F7E651604462C540~plcC8RJbugWa3VOwTFmNZoac2dItOIqZrCA+EHNdMeeS96DZMXNF5vglf64nM6GAvJkyLbbkRbgylTdPz6hhtDkRTjzHzrrjaq2P48FJ0ZbU1GqWQLeikafMJtJiYf7/HTgmd2iUvvXb8eFft1oVC/WjYRvZc680ny4+vY6tlaTd9ds8EkD2B/hjehjmY45u4/Tk2CF2Wbb6vWpDt1rX/CuXVzCa6XiMKnTsWAZOktW4/3p9m3nHgzKEcPxd6w1PsP',
    'fc_vnum': '1',
    'fc_vexp': 'true',
    'gpv_Page': 'https%3A%2F%2Fwww.walgreens.com%2Ffindcare%2Fvaccination%2Fcovid-19%3Fban%3Dcovid_scheduler_brandstory_main_March2021',
    's_sq': 'walgrns%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526link%253DSchedule%252520new%252520appointment%2526region%253DuserOptionButtons%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.walgreens.com%25252Ffindcare%25252Fvaccination%25252Fcovid-19%25252Flocation-screening%2526ot%253DA',
    'dtSa': '-',
    'USER_LOC': '2%2BsKJSc9HtK0OKdV8%2Be6tTufCKUgUi6A%2BRJd8%2BMJ70JBfBetdGRYxnQQ%2BK7rxsqc',
    'gRxAlDis': 'N',
    'dtLatC': '1',
    'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InY1In0.eyJleHAiOjE2MTU5ODI4NjQsImlhdCI6MTYxNTk4MTA2NCwiaXNzIjoid2FsZ3JlZW5zLmNvbSIsImF1ZCI6ImRvdGNvbSIsImp0aSI6ImUyZDZjMTliLWMxZTAtNDU2NC1iZGZhLWM0MjEzYWRkMGJmMyIsInN1YiI6IjIwMDAxNzk1NzE4MSIsImF1dCI6W119.5EHm6K0r_onBzifAd5GIHReBeqpa_bhrKXjRVWywLuA',
    'rxvt': '1615983192458|1615976618232',
    'dtPC': f"5180303804_919h-vFUWNPHCCAQPKITHHEEKVKGDHCFWUAQMB-0e57",
    'akavpau_walgreens': '1615983257~id=8282155e0361b80bd901d89c84bd314d',
    '_abck': 'E77FEE327100289088BFB905986FC20A~0~YAAQBTPFF2NrhD14AQAAtjgYQAVeTKgi1Gk5Zl3hYqOmLzhBlV5KXAPcX5OkWr67sCr+HAfMYYFmySqrTHhKzPcakW1z7LPJqCq855+NqYPCHtWBt412MyxD7NTDb8fsSBIYXXeqLdMDurM9yDDZ8zrMd10QzBoFlvD15/COMK5uJeStZ+qr6m6GfHS7malkHxSmwVIPrYdBZ8qGUYVqUjBLfFHJdwLBPqOHqO+djXnY0ScKbq7JZCSLwJ9PZR9DW8l7Y+11Rzo0rB+ibz4ZDmQupyoeEQSY7eTjU9afaW6Ud4SaHgN6LZq5BovTy0w0NwhzmUMntdSg9+NusiwZf1cdyOEpEHaa5loNn+m9MBvRBULyFYhU4Y4ctvFz9u1t6kGGJPPXNdE4nuF9PvZLtqOhxMjkkvU/L02K~-1~-1~-1',
}

headers2 = {
    'authority': 'www.walgreens.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'x-xsrf-token': 'O40bR0N68x3agA==.CAdba/YsPDeno1kDCLzsQJE77Jp1lPmc9pfpaEqFd2Y=',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.walgreens.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
}



import json
import time
import pprint 
# read file
import os
import datetime 
two_days_from_now = datetime.date.today() + datetime.timedelta(days=2)
date_string = f"{two_days_from_now.year}-{two_days_from_now.month:02d}-{two_days_from_now.day:02d}"

data = {
    '95132':'{"serviceId":"99","position":{"latitude":37.4010609,"longitude":-121.8643855},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    '95014':'{"serviceId":"99","position":{"latitude":37.31317,"longitude":-122.0723816},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    '95060':'{"serviceId":"99","position":{"latitude":37.0105307,"longitude":-122.1178261},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    '94538':'{"serviceId":"99","position":{"latitude":37.5042267,"longitude":-121.9643745},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    '94401':'{"serviceId":"99","position":{"latitude":37.5793536,"longitude":-122.3164207},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    '95815':'{"serviceId":"99","position":{"latitude":37.31317,"longitude":-122.0723816},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25}',
    # '95060':'{"serviceId":"99","position":{"latitude":37.0105307,"longitude":-122.1178261},"appointmentAvailability":{"startDateTime":"2021-03-18"},"radius":25}',
    
}

cities = {
    '95132':'milpitas',
    '95014':'cupertino',
    '95060':'santa cruz',
    '94538':'fremont',
    '94401':'san mateo',
    '95815':'sacremento'
}
d1 = json.loads('{"position":{"latitude":37.31317,"longitude":-122.0723816},"state":"CA","vaccine":{"productId":""},"appointmentAvailability":{"startDateTime":"'+date_string+'"},"radius":25,"size":25,"serviceId":"99"}')


# print(response.text)

from discord_webhooks import DiscordWebhooks
def discord_webhook(message):
  webhook = DiscordWebhooks('https://discord.com/api/webhooks/821277782071443516/toRhNJyNTOwbvyI-vFvh73dCz6VCQxDVT2ZueJOASqU5DJBNx1T-Azac0lSS58HRSXZr')
  webhook.set_content(content=message)
  # webhook.set_content(content=content, title=title, description=description)
  webhook.send()

import pickle
sess = requests.Session()

sess.headers.update(headers2)

cookies3={}
def load_cookies():
    with open('cookies.json', 'r') as myfile:
        data=myfile.read()
        obj = json.loads(data)
        print(obj)
        for cookie in obj:
            pprint.pprint(cookie)
            cookies3[cookie['name']] = cookie['value']
    # exit()
    sess.cookies.update(cookies3)

# parse file
load_cookies()

def reload_cookies():
    os.system("rm -r tmp3")
    os.system("node .\walgreens_login.js")
    load_cookies()
# sess.cookies.update(cookies3)
# reload_cookies()


def lambda_handler(event, context):
    for zipcode, m_data in data.items():
        try:
            # print(m_data)
            response = sess.post('https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability', headers=headers, cookies=cookies, data=m_data)
        
            res = json.loads(response.text)
            appointmentsAvailable = False
            if(res['appointmentsAvailable']==True):
                appointmentsAvailable = True
                print(f"walgreens appointment available in {cities[zipcode]}! {zipcode}"+response.text)
                print(res)
            else: 
                print("no appointment available for",zipcode)
            d1['position'] = json.loads(m_data)['position']
            # print(json.dumps(d1))
            d2  = '{"position":{"latitude":37.5042267,"longitude":-121.9643745},"state":"CA","vaccine":{"productId":""},"appointmentAvailability":{"startDateTime":"2021-03-17"},"radius":25,"size":25,"serviceId":"99"}'

            response2 = sess.post('https://www.walgreens.com/hcschedulersvc/svc/v2/immunizationLocations/timeslots', data=json.dumps(d1))
            
            print('response2.status_code',response2.status_code)
            if response2.status_code == 404:
                print('timeslots for',zipcode, response2.status_code,'body=',response2.text)
                # print('response2.text',response2.text)
                continue

            if response2.status_code == 401:
                print('cookie expired!')
                reload_cookies()
                continue

            
            if response2.status_code == 200:
                print(response2.text)
                res2 = json.loads(response2.text)
                if 'locations' in res2 and len(res2['locations']) >0:
                    if appointmentsAvailable:
                        output = f"{cities[zipcode]}, {zipcode}:\n"
                        # print(f"{cities[zipcode]} {zipcode}:")
                        for location in a['locations']:
                            # location = json.loads('{"locations":[{"locationId":"b90757e3-d4e0-43c6-9d94-f3a7f927cbf8","name":"Walgreen Drug Store","partnerLocationId":"3185","description":"","logoURL":"/images/adaptive/pharmacy/healthcenter/health-navigator/Walgreens_logo_2X.png","distance":7.69,"position":{"latitude":37.78505291,"longitude":-122.4063133},"address":{"line1":"825 MARKET ST","line2":"","city":"SAN FRANCISCO","state":"CA","country":"US","zip":"94103"},"categories":[{"code":"2","display":"Immunizations","services":[{"code":"99","display":"COVID-19 Vaccine"}]}],"orgId":"Organization/35860656-84da-43fd-b66f-47e81b483e3b","phone":[{"type":"StorePrimary","number":"415-543-9502"},{"type":"StoreSecondary","number":""},{"type":"Pharmacy","number":"415-543-9502"}],"fhirLocationId":"b90757e3-d4e0-43c6-9d94-f3a7f927cbf8","storenumber":"3185","manufacturer":[{"productId":"5fd1ab9f5fa47e056c076ff2","name":"Pfizer-BioNtech"}],"appointmentAvailability":[{"date":"2021-03-25","day":"Thursday","slots":["03:45 pm","04:00 pm","04:15 pm","04:30 pm","04:45 pm","05:30 pm"]}]},{"locationId":"296f939f-b0f4-4479-935b-4a8856f65c97","name":"Walgreen Drug Store","partnerLocationId":"890","description":"","logoURL":"/images/adaptive/pharmacy/healthcenter/health-navigator/Walgreens_logo_2X.png","distance":7.75,"position":{"latitude":37.78600923,"longitude":-122.40829713},"address":{"line1":"135 POWELL ST","line2":"","city":"SAN FRANCISCO","state":"CA","country":"US","zip":"94102"},"categories":[{"code":"2","display":"Immunizations","services":[{"code":"99","display":"COVID-19 Vaccine"}]}],"orgId":"Organization/35860656-84da-43fd-b66f-47e81b483e3b","phone":[{"type":"StorePrimary","number":"415-391-7222"},{"type":"StoreSecondary","number":"415-391-7224"},{"type":"Pharmacy","number":"415-391-7222"}],"fhirLocationId":"296f939f-b0f4-4479-935b-4a8856f65c97","storenumber":"890","manufacturer":[{"productId":"5fd1ab9f5fa47e056c076ff2","name":"Pfizer-BioNtech"}],"appointmentAvailability":[{"date":"2021-03-25","day":"Thursday","slots":["04:30 pm","04:45 pm"]}]},{"locationId":"614984b6-1c74-4cca-bd2c-0e8923b16b24","name":"Walgreen Drug Store","partnerLocationId":"4275","description":"","logoURL":"/images/adaptive/pharmacy/healthcenter/health-navigator/Walgreens_logo_2X.png","distance":7.11,"position":{"latitude":37.78999645,"longitude":-122.39758774},"address":{"line1":"456 MISSION ST","line2":"","city":"SAN FRANCISCO","state":"CA","country":"US","zip":"94105"},"categories":[{"code":"2","display":"Immunizations","services":[{"code":"99","display":"COVID-19 Vaccine"}]}],"orgId":"Organization/35860656-84da-43fd-b66f-47e81b483e3b","phone":[{"type":"StorePrimary","number":"415-348-9600"},{"type":"StoreSecondary","number":"415-348-9436"},{"type":"Pharmacy","number":"415-348-9600"}],"fhirLocationId":"614984b6-1c74-4cca-bd2c-0e8923b16b24","storenumber":"4275","manufacturer":[{"productId":"5fd1ab9f5fa47e056c076ff2","name":"Pfizer-BioNtech"}],"appointmentAvailability":[{"date":"2021-03-25","day":"Thursday","slots":["04:15 pm","04:30 pm","04:45 pm","05:00 pm"]}]},{"locationId":"f7510749-d3f6-4f77-ba76-18f25ae250ae","name":"Walgreen Drug Store","partnerLocationId":"2866","description":"","logoURL":"/images/adaptive/pharmacy/healthcenter/health-navigator/Walgreens_logo_2X.png","distance":9.41,"position":{"latitude":37.78217087,"longitude":-122.43961304},"address":{"line1":"1363 DIVISADERO ST","line2":"","city":"SAN FRANCISCO","state":"CA","country":"US","zip":"94115"},"categories":[{"code":"2","display":"Immunizations","services":[{"code":"99","display":"COVID-19 Vaccine"}]}],"orgId":"Organization/35860656-84da-43fd-b66f-47e81b483e3b","phone":[{"type":"StorePrimary","number":"415-931-9974"},{"type":"StoreSecondary","number":""},{"type":"Pharmacy","number":"415-931-9974"}],"fhirLocationId":"f7510749-d3f6-4f77-ba76-18f25ae250ae","storenumber":"2866","manufacturer":[{"productId":"5fd1ab9f5fa47e056c076ff2","name":"Pfizer-BioNtech"}],"appointmentAvailability":[{"date":"2021-03-25","day":"Thursday","slots":["03:45 pm","04:00 pm","04:15 pm","04:30 pm","04:45 pm","05:00 pm","05:15 pm","05:30 pm"]}]},{"locationId":"44d8f131-f60f-48a3-bc35-0e83659bb5b5","name":"Walgreen Drug Store","partnerLocationId":"2152","description":"","logoURL":"/images/adaptive/pharmacy/healthcenter/health-navigator/Walgreens_logo_2X.png","distance":8.98,"position":{"latitude":37.78681943,"longitude":-122.43366362},"address":{"line1":"1899 FILLMORE ST","line2":"","city":"SAN FRANCISCO","state":"CA","country":"US","zip":"94115"},"categories":[{"code":"2","display":"Immunizations","services":[{"code":"99","display":"COVID-19 Vaccine"}]}],"orgId":"Organization/35860656-84da-43fd-b66f-47e81b483e3b","phone":[{"type":"StorePrimary","number":"415-771-4603"},{"type":"StoreSecondary","number":""},{"type":"Pharmacy","number":"415-771-4603"}],"fhirLocationId":"44d8f131-f60f-48a3-bc35-0e83659bb5b5","storenumber":"2152","manufacturer":[{"productId":"5fd1ab9f5fa47e056c076ff2","name":"Pfizer-BioNtech"}],"appointmentAvailability":[{"date":"2021-03-25","day":"Thursday","slots":["04:45 pm"]}]}]}')
                            output += f"{location['name']}, {location['address']['line1']}, {location['address']['city']} has "
                            output += str(len(location['appointmentAvailability'][0]['slots'])) +' timeslot(s) available for '
                            output += f"{location['manufacturer'][0]['name']}. on {location['appointmentAvailability'][0]['date']}\n"
                        print(f"walgreens appointments and vaccine inventory available in {cities[zipcode]}! {zipcode}")
                        print(response.text)
                        discord_webhook(output)

        except Exception as inst:
            # raise inst
            print(inst)
            pass

    return {
        'statusCode': 200,
        'body': json.dumps('ok')
    }
# import discord
retry = True
while retry:
    lambda_handler(None,None)
    time.sleep(45)