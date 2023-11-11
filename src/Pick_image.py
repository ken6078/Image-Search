from label_trans import keyword_search
from photohash import hash_distance, average_hash

import random
import csv
from PIL import Image

class Pick_image():
    def __init__(self) -> None:
        self.keyword_search = keyword_search()

        self.labels = {}
        labelListfile = open('assets/labelList.txt', 'r', encoding="utf-8")
        spamreader = csv.reader(labelListfile, quotechar=',')
        for row in spamreader:
            if row[1] not in self.labels:
                self.labels[row[1]] = [row[0]]
            else:
                self.labels[row[1]].append(row[0])
        
        self.images = {}
        imageListfile = open('assets/imageList.txt', 'r', encoding="utf-8")
        spamreader = csv.reader(imageListfile, quotechar=',')
        for row in spamreader:
            self.images[row[0]] = [row[1], row[2]]

    def pick_images_with_keyword(self, keyword: str, seed: int = None) -> []:
        if type(seed) == int:
            random.seed(seed)
        labelName = self.keyword_search.search(keyword)
        resultImageIDs = random.sample(self.labels[labelName], 20)
        resultIMageURLs = []
        for imageID in resultImageIDs:
            resultIMageURLs.append(self.images[imageID][1])
        return resultIMageURLs

    def pick_images_with_image(self, image: Image, seed: int = None):
        if type(seed) == int:
            random.seed(seed)
        image = image.resize((8, 8), Image.Resampling.LANCZOS).convert('L')
        hash = average_hash(image)
        result = []
        for i in self.images:
            distance = hash_distance(hash, self.images[i][0])
            if len(result) < 10:
                result.append([distance, self.images[i][0],self.images[i][1]])
            else:
                if distance < result[-1][0]:
                    result.append([distance, self.images[i][0],self.images[i][1]])
                result.pop()
                result.sort()
        return [row[2] for row in result]