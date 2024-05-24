## Text document clustering (Json, Yaml, XML)
---

This project was prepared as a training project after completing a course on NLP.

Often in large informational-systems there are data channels that require an estimate of the number of types of transmitted documents.
This project aims to identify the types of documents passing through the data channel.

### Model Description}
Baseline model for this project is Doc2Vec that allows you to get a perfect combination of high performance and minimum system requirements for such a task.

### Dataset
Data set is a randomly generated text-based documents of differ types: json, xml, yaml.
You can choose the number of different documents type and degree of mixin data.

### Experiment Setup

- Generating of text documents with some mixins from doc to doc
- Reading generated docs 
- Extracting docs keys
- Embedding group of doc keys as tagged data for Doc2Vec model
- Train Doc2Vec model
- Clustering with DBSCAN method
- Clustering with BIRCH method
- Compare results with generating docs parameters
