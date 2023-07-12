
docker run -d --name elastic \
    -v /Users/maximer/Documents/Dev/Python/Projets/elasticsearch-nlp-sentiment_analysis/elastic_search/data:/usr/share/elasticsearch/data \
    --net elastic \
    -p 9200:9200 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10


curl -X DELETE "http://localhost:9200/textes"

curl -X PUT "localhost:9200/textes" -H 'Content-Type: application/json' -d'
{
    "settings": {
        "index": {
            "analysis": {  
                "analyzer": {
                    "my_analyzer": {
                        "type": "standard"
                    }
                }
            }
        }
    },
    "mappings": {
        "properties": {
        "patient_id": {
            "type": "integer"
        },
        "text": {
            "type": "text",
            "analyzer": "standard"
        },
        "date": {
            "type": "date"
        },
        "emotion": {
            "type": "keyword"
        },
        "confidence": {
            "type": "float"
        }
        }
    }
}
'