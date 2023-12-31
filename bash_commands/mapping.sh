#!/bin/sh
curl -X DELETE "http://localhost:9200/notes"

curl -X PUT "localhost:9200/notes" -H 'Content-Type: application/json' -d'
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