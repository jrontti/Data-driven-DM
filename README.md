Welcome to Github my Github page. This repository is used for Data-Driven Decision Making for Smart Cities and Businesses- course

Elasticsearch + Kibana personal guide and cheat sheet for personal set up

1. Get on cmd and get Elastic & Kibana

cd below
Elasticsearch dir:
C:\Users\Jesse\Documents\DDM 2021\elasticsearch-7.12.0

Kibana dir:
C:\Users\Jesse\Documents\DDM 2021\kibana-7.12.0-windows-x86_64

2. Run Elasticsearch & Kibana

run Elasticsearch

.\bin\elasticsearch.bat

run kibana

.\bin\kibana.bat

More about Kibana : https://www.elastic.co/guide/en/kibana/7.12/windows.html

3. Check if those are working 

curl http://localhost:9200

curl http://localhost:5601

4. Go to via browser

http://localhost:9200

http://localhost:5601

################################################

Setting up ELK cluster in Pouta

Cluster architecture:
node 1: master node
node 2: data node
node 3: data node
node 4: ingest node




