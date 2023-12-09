import json

INPUT_FILE = 'input.json'
OUTPUT_FILE = 'output.json'

def filterJson(jsonData):
    aggregatedVulns = {}
    resultJson = {"vulnerabilities": []}
    for alert in jsonData['alerts']:
        vulName = alert['name']
        aggregatedVulns[vulName] = aggregatedVulns.get(vulName, 0) + 1
    for vulname, vulcount in aggregatedVulns.items():
        newVul = {'name': vulname, 'count': vulcount}
        resultJson['vulnerabilities'].append(newVul)
    return resultJson


if __name__ == "__main__":

    # Откроем и отфильтруем JSON
    try:
        with open(INPUT_FILE, 'r') as file:
            jsonData = json.load(file)
            filteredJson = filterJson(jsonData)
    except:
        print(f'Не удалось открыть файл {INPUT_FILE} или произошла ошибка при обработке JSON')

    # Сохраним полученные результаты
    try:
        with open(OUTPUT_FILE, 'w') as outfile:
            json.dump(filteredJson, outfile, indent=4)
        print(f'Результат сохранен в файл {OUTPUT_FILE}')
    except:
        print(f'Не удалось открыть файл {OUTPUT_FILE} для сохранения результатов')