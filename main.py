import json
wikipedia_link = 'https://en.wikipedia.org/wiki/'
class Iteration_json:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file, encoding='utf-8') as f:
            file_json = json.load(f)

            for name in file_json:
                country = name['name']['common']
                country_dash = country.replace(' ', '_')
                print(country + ' - ' + wikipedia_link + country_dash)
                unification = country + ' - ' + wikipedia_link + country_dash + '\n'
            if len(country) == len(country):
                raise StopIteration
            return unification

    def download (self, file_path):
        with open(file_path, 'a', encoding='utf-8') as new_file:
            for data in self:
                new_file.write(data)
                new_file.close()

if __name__ == '__main__':
    downloader = Iteration_json('countries.json')
    downloader.download('countries_links.txt')



