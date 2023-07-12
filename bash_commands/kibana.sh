

docker run \
    --name kib01-test \
    --net elastic \
    -p 127.0.0.1:5601:5601 \
    -e "ELASTICSEARCH_HOSTS=http://elastic:9200" docker.elastic.co/kibana/kibana:7.17.11
