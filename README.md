# Named Entity Regonition System
This is a template code for a Named Entity Recognition system using Spacy V3

# What does the code in this repo do
The code in this repo in particular performs data preprocessing and exporting the data in .spacy format, configs required to train a spacy NER model and perform inference with the trained NER model.

# Set up environment 
* Requirement: ```anaconda```, ```pip```, ```python 3```
* It is a good practice to create a new conda environment and here is how to create one:
  ```
  conda create -n "name_of_new_environment" python==3.8.5
  conda activate "name_of_new_environment"
  ```
* Install dependencies (use Anaconda Prompt): 
  ```
  pip install --upgrade pip 
  pip install spacy
  ```
  
# Preprocess the data and create training/test sets in .spacy format

Ensure your current directory has all the files from this repo.
```
python ner - data preprocessing.py

```

# Train the custom NER model (training is done via the CLI in Spacy v3 - it is cool)

Follow the instruction in here https://spacy.io/usage/training and create a base_config.cfg for a custom NER model.

Then input the location of your train and test sets in the base_config.cfg file.

Afterwards, run the following code to update the rest of the parameters in the base_config.cfg file.

```
python -m spacy init fill-config base_config.cfg config.cfg

```

Once that is done, run the following code to train your model.

```
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./test.spacy

```
Above code will create a directory named "output" in your current directory and you will find the directories "model-best" and "model-last" inside of this directory.


# Perform inferencing with the newly trained model

Ensure your current directory has all the files from this repo.
```
python ner - inference.py

```

  

