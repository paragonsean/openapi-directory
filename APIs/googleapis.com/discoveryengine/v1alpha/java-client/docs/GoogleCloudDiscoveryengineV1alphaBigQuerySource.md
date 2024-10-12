

# GoogleCloudDiscoveryengineV1alphaBigQuerySource

BigQuery source import data from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSchema** | **String** | The schema to use when parsing the data from the source. Supported values for user event imports: * &#x60;user_event&#x60; (default): One UserEvent per row. Supported values for document imports: * &#x60;document&#x60; (default): One Document format per row. Each document must have a valid Document.id and one of Document.json_data or Document.struct_data. * &#x60;custom&#x60;: One custom data per row in arbitrary format that conforms to the defined Schema of the data store. This can only be used by Gen App Builder. |  [optional] |
|**datasetId** | **String** | Required. The BigQuery data set to copy the data from with a length limit of 1,024 characters. |  [optional] |
|**gcsStagingDir** | **String** | Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the BigQuery export to a specific Cloud Storage directory. |  [optional] |
|**partitionDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**projectId** | **String** | The project ID (can be project # or ID) that the BigQuery source is in with a length limit of 128 characters. If not specified, inherits the project ID from the parent request. |  [optional] |
|**tableId** | **String** | Required. The BigQuery table to copy the data from with a length limit of 1,024 characters. |  [optional] |



