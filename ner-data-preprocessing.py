import spacy
from tqdm import tqdm
from spacy.tokens import DocBin

train = [
    ("I wont make it on Friday, 9/10.", {"entities": [(17, 30, "DATE")]}),
    ("I wont make it on Friday, 9/10/21", {"entities": [(17, 33, "DATE")]}),
    ("I need to cancel my shift for the 10th", {"entities": [(34, 38, "DATE")]}),
    ("I wont make it on Monday, 11/10", {"entities": [(17, 31, "DATE")]}),
    ("I wont make it on Tuesday, 12/10/21", {"entities": [(17, 35, "DATE")]}),
    ("I need to cancel my shift for the 10th", {"entities": [(34, 38, "DATE")]}),
    ("I need to cancel my shift on the 10th.", {"entities": [(33, 37, "DATE")]}),
    ("I wont make it on Friday, the 10", {"entities": [(17, 32, "DATE")]}),
    ("I wont make it on Monday, the 12", {"entities": [(17, 32, "DATE")]}),
    ("I will make it on Wednesday, the 10th", {"entities": [(18, 37, "DATE")]}),
    ("I wont make it on Friday 9/10", {"entities": [(17, 29, "DATE")]}),
    ("I wont make it on Friday 9/10/21", {"entities": [(17, 32, "DATE")]}),
    ("I need to cancel my shift for the 10th", {"entities": [(34, 38, "DATE")]}),
    ("I wont make it on Monday 11/10", {"entities": [(17, 30, "DATE")]}),
    ("I wont make it on Tuesday 12/10/21.", {"entities": [(17, 34, "DATE")]}),
    ("I need to cancel my shift for the 15th.", {"entities": [(34, 38, "DATE")]}),
    ("I wont make it on Friday the 10.", {"entities": [(17, 31, "DATE")]}),
    ("I wont make it on Monday the 12", {"entities": [(17, 31, "DATE")]}),
    ("I wont make it on Wednesday the 10th", {"entities": [(18, 36, "DATE")]}),
    ("I am out of town 9/15", {"entities": [(17, 21, "DATE")]}),
    ("I am out of town 9/15/21", {"entities": [(17, 24, "DATE")]}),
    ('Jason Adams wont make it to work on the 15th', {"entities": [(40, 44, "DATE")]}),
    ('Michael B. Jordan wont make it to work on the 22nd', {"entities": [(46, 50, "DATE")]}),
    ('Michael B. Jordan wont make it to work on the 22nd and 23rd.',
     {"entities": [(46, 50, "DATE"), (55, 59, "DATE")]}),
    ('Michael B. Jordan wont make it to work on the 1st and 5th', {"entities": [(46, 49, "DATE"), (54, 57, "DATE")]}),
    ('I wont make it to work on 10/12/21 and 10/25/21', {"entities": [(26, 34, "DATE"), (39, 47, "DATE")]}),
    ('He wont make it to work on the 22nd.', {"entities": [(31, 35, "DATE")]}),
    ("Hey boss Michael won't make it to Hawaii on 10/31/21. 1 billion dollars is too much",
     {"entities": [(44, 52, "DATE")]}),
    ('I will be out of town on 11.12.21', {"entities": [(25, 33, "DATE")]}),
    ('She is away from the 25th to the 31st', {"entities": [(21, 25, "DATE"), (33, 37, "DATE")]}),
    ('They are only here from 4/1/21 to 4/22/21', {"entities": [(24, 30, "DATE"), (34, 41, "DATE")]}),
    ('They are only here from 4.1.21 to 4.22.21', {"entities": [(24, 30, "DATE"), (34, 41, "DATE")]}),
    ("Walmart is a leading e-commerce company", {"entities": [(0, 7, "ORG")]}),
    ("I reached Chennai yesterday.", {"entities": [(19, 28, "GPE")]}),
    ("I recently ordered a book from Amazon", {"entities": [(24,32, "ORG")]}),
    ("I was driving a BMW", {"entities": [(16,19, "PRODUCT")]}),
    ("I ordered this from ShopClues", {"entities": [(20,29, "ORG")]}),
    ("Fridge can be ordered in Amazon ", {"entities": [(0,6, "PRODUCT")]}),
    ("I bought a new Washer", {"entities": [(16,22, "PRODUCT")]}),
    ("I bought a old table", {"entities": [(16,21, "PRODUCT")]}),
    ("I bought a fancy dress", {"entities": [(18,23, "PRODUCT")]})
]

test = [
    ("I wont make it on Tuesday, 9/10", {"entities": [(17, 30, "DATE")]}),
    ("I wont make it on Wednesday 9/10/21", {"entities": [(17, 35, "DATE")]}),
    ("I need to cancel my shift for the 10th", {"entities": [(34, 38, "DATE")]}),
    ("I wont make it on Monday, 11/10", {"entities": [(17, 31, "DATE")]}),
    ("I wont make it on Tuesday, 12/10/21", {"entities": [(17, 35, "DATE")]}),
    ("I need to cancel my shift for the 10th", {"entities": [(34, 38, "DATE")]}),
    ("I need to cancel my shift on the 10th", {"entities": [(33, 37, "DATE")]}),
    ("I wont make it on the 10", {"entities": [(22, 24, "DATE")]}),
    ("I wont make it on the 12", {"entities": [(22, 24, "DATE")]}),
    ("I wont make it on 25th", {"entities": [(18, 22, "DATE")]}),
    ("I am out of town 10/31.", {"entities": [(17, 22, "DATE")]}),
    ('Harry isnt coming on the 4th and 5th', {"entities": [(25, 28, "DATE"), (33, 36, "DATE")]}),
    ('I will be out of town on 1.1.21', {"entities": [(25, 31, "DATE")]}),
    ("I rented a camera", {"entities": [(12,18, "PRODUCT")]}),
    ("I rented a tent for our trip", {"entities": [(12,16, "PRODUCT")]}),
    ("I rented a screwdriver from our neighbour", {"entities": [(12,22, "PRODUCT")]}),
    ("I repaired my computer", {"entities": [(15,23, "PRODUCT")]}),
    ("I got my clock fixed", {"entities": [(16,21, "PRODUCT")]}),
    ("I got my truck fixed", {"entities": [(16,21, "PRODUCT")]}),
    ("Flipkart started it's journey from zero", {"entities": [(0,8, "ORG")]}),
    ("I recently ordered from Max", {"entities": [(24,27, "ORG")]}),
    ("Flipkart is recognized as leader in market",{"entities": [(0,8, "ORG")]}),
    ("I recently ordered from Swiggy", {"entities": [(24,29, "ORG")]})

]

package = {"train": train,
            "test": test}

# load a new blank spacy model
nlp = spacy.blank("en")

# Spacy v3.1, however, no longer takes this format and this has to be converted to their .spacy format by
# first converting these in doc and then a docbin
# create a DocBin object
db = DocBin()

for name, data in package.items():
    for text, annotation in tqdm(data):
        doc = nlp(text)
        ents = []
        for start, end, label in annotation['entities']:
            span = doc.char_span(start, end, label=label)
            if span is None:
                print("Skipping")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk("./data/{}.spacy".format(name))



