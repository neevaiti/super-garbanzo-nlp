# obtenir la liste des index d'une connexion
curl -X GET "http://localhost:9200/_cat/indices?v"

# Health : Indique l'état de santé du cluster Elasticsearch par rapport à l'index. Les valeurs possibles sont green (vert), yellow (jaune) et red (rouge). green signifie que tous les nœuds de données contiennent toutes les copies de l'index, yellow signifie que toutes les copies primaires sont disponibles, mais certaines copies répliques ne le sont pas, et red signifie que certaines données sont indisponibles.
# Status : Indique l'état d'ouverture de l'index. open signifie que l'index est ouvert et accessible pour les opérations de lecture/écriture.
# UUID : L'identifiant unique de l'index.
# Primary shards : Le nombre de shards primaires utilisés pour stocker l'index.
# Replica shards : Le nombre de shards répliques utilisés pour stocker l'index.
# docs.count : Le nombre total de documents dans l'index.
# docs.deleted : Le nombre de documents supprimés dans l'index.
# store.size : La taille totale du stockage utilisé par l'index, y compris les données primaires et les répliques.
# pri.store.size : La taille du stockage primaire utilisé par l'index, qui exclut les répliques.