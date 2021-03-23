import json
wikipedia_link = 'https://en.wikipedia.org/wiki/'
class Iteration_json:
    def __init__(self, file):
        self.file = file
        self.start = 0
        self.len_f = len(self.file)
        f_j = open('countries.json', encoding='utf-8')
        self.file_json = json.load(f_j)
    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        try:
            self.start <= self.len_f
        except IndexError:
            raise StopIteration
        country = self.file_json[self.start]['name']['common']
        country_dash = country.replace(' ', '_')
        unification = country + ' - ' + wikipedia_link + country_dash + '\n'
        return unification

    def download(self, file_path):
        with open(file_path, 'a', encoding='utf-8') as new_file:
            for data in self:
                new_file.write(data)
                # new_file.close()

if __name__ == '__main__':
    downloader = Iteration_json('contries.json')
    downloader.download('countries_links_1.txt')
    for t in downloader:
        print(t)




