# VertexAiApi.GoogleCloudAiplatformV1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationBigqueryUri** | **String** | URI of desired destination BigQuery table. Expected format: &#x60;bq://{project_id}:{dataset_id}:{table}&#x60; If not specified, then results are exported to the following auto-created BigQuery table: &#x60;{project_id}:export_evaluated_examples_{model_name}_{yyyy_MM_dd&#39;T&#39;HH_mm_ss_SSS&#39;Z&#39;}.evaluated_examples&#x60; | [optional] 
**overrideExistingTable** | **Boolean** | If true and an export destination is specified, then the contents of the destination are overwritten. Otherwise, if the export destination already exists, then the export operation fails. | [optional] 


