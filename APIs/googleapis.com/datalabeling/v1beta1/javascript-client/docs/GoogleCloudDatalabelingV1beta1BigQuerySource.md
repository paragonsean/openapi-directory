# DataLabelingApi.GoogleCloudDatalabelingV1beta1BigQuerySource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputUri** | **String** | Required. BigQuery URI to a table, up to 2,000 characters long. If you specify the URI of a table that does not exist, Data Labeling Service creates a table at the URI with the correct schema when you create your EvaluationJob. If you specify the URI of a table that already exists, it must have the [correct schema](/ml-engine/docs/continuous-evaluation/create-job#table-schema). Provide the table URI in the following format: \&quot;bq://{your_project_id}/ {your_dataset_name}/{your_table_name}\&quot; [Learn more](/ml-engine/docs/continuous-evaluation/create-job#table-schema). | [optional] 


