import json

with open('output.csv', 'w') as csv_file:
    with open("/home/mahkam/Desktop/Django/creativetravel/partner_feed_ru.json", encoding="UTF-8") as json_file:
        for line in json_file:
            data = json.loads(line)
            csv_file.write(';'.join([data['id']]))
