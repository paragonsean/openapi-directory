

# GooglePrivacyDlpV2BigQueryTable

Message defining the location of a BigQuery table. A table is uniquely identified by its project_id, dataset_id, and table_name. Within a query a table is often referenced with a string in the format of: `:.` or `..`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetId** | **String** | Dataset ID of the table. |  [optional] |
|**projectId** | **String** | The Google Cloud Platform project ID of the project containing the table. If omitted, project ID is inferred from the API call. |  [optional] |
|**tableId** | **String** | Name of the table. |  [optional] |



