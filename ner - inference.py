import spacy

nlp = spacy.load("./output/model-last")
doc = nlp("She is only here from 4.1.21 to 4.22.21'")
print("Entities: ", [{"entity": ent.label_, "value": ent.text} for ent in doc.ents])
