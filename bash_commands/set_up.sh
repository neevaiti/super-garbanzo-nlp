#!/bin/bash

docker run -d --name elastic \
    -v /Users/charles/Documents/pythonProject/elasticsearch-nlp-sentiment_analysis/elastic_search/data:/usr/share/elasticsearch/data \
    --net elastic \
    -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10



docker run --name kib01-test --net elastic -p 127.0.0.1:5601:5601 \
-e "ELASTICSEARCH_HOSTS=http://elastic:9200" docker.elastic.co/kibana/kibana:7.17.10
