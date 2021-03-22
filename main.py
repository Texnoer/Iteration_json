import json
wikipedia_link = 'https://en.wikipedia.org/wiki/'
class Iteration_json:
    def __init__(self, file, start):
        self.file = file
        self.start = start
        ft = open(self.file, encoding='utf-8')
        self.file_json = json.load(ft)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        try:
            self.file_json[self.start]
        except IndexError:
            raise StopIteration
        for name in self.file_json:
            country = name['name']['common']
            country_dash = country.replace(' ', '_')
            print(country + ' - ' + wikipedia_link + country_dash)
            unification = country + ' - ' + wikipedia_link + country_dash + '\n'
        return unification

    def download (self, file_path):
        with open(file_path, 'a', encoding='utf-8') as new_file:
            for data in self:
                new_file.write(data)
            new_file.close()

if __name__ == '__main__':
    downloader = Iteration_json('countries.json', 0)
    downloader.download('countries_links_1.txt')



