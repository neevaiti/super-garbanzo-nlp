
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

# Psychologist's Website - Sentiment Detection

### Super-Garbanzo-NLP - NLP Model:

Super-Garbanzo-NLP is a web application designed to assist mental health professionals in their daily practice. The application utilizes their patients' daily writings to analyze the emotions expressed therein. 
Thanks to the power of artificial intelligence provided by this [model](https://huggingface.co/SamLowe/roberta-base-go_emotions) from Hugging Face, the tool scans journal entries and detects the primary emotions contained within the text. The information gathered is then stored in an Elasticsearch database, allowing for quick access and in-depth data analysis.
All of this is complemented by a PostgreSQL database.

This tool has been designed with a particular focus on efficiency and ease of use. Therefore, professionals can get an overview of their patients' emotional state between sessions without having to read every journal entry in detail.


## Useful Documentation

- [Docker](https://www.docker.com/)
- [Elastic Search](https://www.elastic.co/fr/elasticsearch/)
- [Pandas](https://pandas.pydata.org/docs/index.html)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](https://scikit-learn.org/stable/) 
- [Python](https://docs.python.org/3/)
- [Hugging Face](https://huggingface.co/)


## Requirements

You can install the necessary packages via the requirements.txt file for use notebooks locally.

```sh
pip install -r requirements.txt
```


### Launching with Docker

With [Docker](https://www.docker.com/), you have everything you need to create containers and download images in the docker-compose.yml file.

#### 1 - Build the docker-compose

```sh
docker-compose build
```

#### 2 - Launch the docker-compose

```sh
docker-compose up
```

#### 3 - Once everything is accessible

Make sure to run the mapping.sh file to index the Elastic Search database.

You can do this with the following command in the directory where the bash_commands file is located:
```sh
sh mapping.sh
```


    
## Authors

- [@MaximeR12](https://github.com/MaximeR12)
- [@neevaiti](https://github.com/neevaiti)