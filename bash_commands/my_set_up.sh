#!/bin/bash

docker run -d --name elastic \
    -v /Users/maximer/Documents/Dev/Python/Projets/elasticsearch-nlp-sentiment_analysis/elastic_search/data:/usr/share/elasticsearch/data \
    --net elastic \
    -p 9200:9200 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10