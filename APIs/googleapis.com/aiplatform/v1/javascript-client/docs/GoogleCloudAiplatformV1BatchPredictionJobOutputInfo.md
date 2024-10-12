# VertexAiApi.GoogleCloudAiplatformV1BatchPredictionJobOutputInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryOutputDataset** | **String** | Output only. The path of the BigQuery dataset created, in &#x60;bq://projectId.bqDatasetId&#x60; format, into which the prediction output is written. | [optional] [readonly] 
**bigqueryOutputTable** | **String** | Output only. The name of the BigQuery table created, in &#x60;predictions_&#x60; format, into which the prediction output is written. Can be used by UI to generate the BigQuery output path, for example. | [optional] [readonly] 
**gcsOutputDirectory** | **String** | Output only. The full path of the Cloud Storage directory created, into which the prediction output is written. | [optional] [readonly] 


