import requests

def get_starships():
    counter = 0
    count = 1
    lst_starships = []
    page = 1
    temp = []  #list for crew sizes that aren't numeric

    while counter != count:
        data = requests.get("https://swapi.dev/api/starships?page=%s" % page)
        response = data.json()

        if response:
            count = response['count']
            result = response['results']

            for starship in result:
                name = starship['name']
                crew = starship['crew'].replace(',', '')

                if crew.isnumeric():
                    lst_starships.append([name, int(crew)])
                else:
                    temp.append([name, crew])

            counter = counter + len(result)
            page += 1
        else:
            print('An error has occurred.')
            break

    lst_starships.sort(key=lambda x: x[1])
    lst_starships.extend(temp)

    return lst_starships
