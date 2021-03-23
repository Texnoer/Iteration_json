import json
wikipedia_link = 'https://en.wikipedia.org/wiki/'
class Iteration_json:
    def __init__(self, file):
        self.file = file
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        try:
            self.start == len(self.file)
        except IndexError:
            raise StopIteration
        return self.file

    def download (self, file_path):
        with open(file_path, 'a', encoding='utf-8') as new_file:
            for data in self:
                new_file.write(data)
                new_file.close()

if __name__ == '__main__':
    ft = open('countries.json', encoding='utf-8')
    file_json = json.load(ft)
    for name in file_json:
        country = name['name']['common']
        country_dash = country.replace(' ', '_')
        print(country + ' - ' + wikipedia_link + country_dash)
        unification = country + ' - ' + wikipedia_link + country_dash + '\n'
        downloader = Iteration_json(unification)
        downloader.download('countries_links_1.txt')



