

# GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequestGcsTrainingInput

Cloud Storage training data input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corpusDataPath** | **String** | The Cloud Storage corpus data which could be associated in train data. The data path format is gs:///. A newline delimited jsonl/ndjson file. For search-tuning model, each line should have the _id, title and text. Example: {\&quot;_id\&quot;: \&quot;doc1\&quot;, title: \&quot;relevant doc\&quot;, \&quot;text\&quot;: \&quot;relevant text\&quot;} |  [optional] |
|**queryDataPath** | **String** | The gcs query data which could be associated in train data. The data path format is gs:///. A newline delimited jsonl/ndjson file. For search-tuning model, each line should have the _id and text. Example: {\&quot;_id\&quot;: \&quot;query1\&quot;, \&quot;text\&quot;: \&quot;example query\&quot;} |  [optional] |
|**testDataPath** | **String** | Cloud Storage test data. Same format as train_data_path. If not provided, a random 80/20 train/test split will be performed on train_data_path. |  [optional] |
|**trainDataPath** | **String** | Cloud Storage training data path whose format should be gs:///. The file should be in tsv format. Each line should have the doc_id and query_id and score (number). For search-tuning model, it should have the query-id corpus-id score as tsv file header. The score should be a number in [0, inf+). The larger the number is, the more relevant the pair is. Example: query-id\\tcorpus-id\\tscore query1\\tdoc1\\t1 |  [optional] |



