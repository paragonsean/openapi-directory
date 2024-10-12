

# GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest

Request message for Import methods.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoGenerateIds** | **Boolean** | Whether to automatically generate IDs for the documents if absent. If set to &#x60;true&#x60;, Document.ids are automatically generated based on the hash of the payload, where IDs may not be consistent during multiple imports. In which case ReconciliationMode.FULL is highly recommended to avoid duplicate contents. If unset or set to &#x60;false&#x60;, Document.ids have to be specified using id_field, otherwise, documents without IDs fail to be imported. Only set this field when using GcsSource or BigQuerySource, and when GcsSource.data_schema or BigQuerySource.data_schema is &#x60;custom&#x60; or &#x60;csv&#x60;. Otherwise, an INVALID_ARGUMENT error is thrown. |  [optional] |
|**bigquerySource** | [**GoogleCloudDiscoveryengineV1alphaBigQuerySource**](GoogleCloudDiscoveryengineV1alphaBigQuerySource.md) |  |  [optional] |
|**errorConfig** | [**GoogleCloudDiscoveryengineV1alphaImportErrorConfig**](GoogleCloudDiscoveryengineV1alphaImportErrorConfig.md) |  |  [optional] |
|**gcsSource** | [**GoogleCloudDiscoveryengineV1alphaGcsSource**](GoogleCloudDiscoveryengineV1alphaGcsSource.md) |  |  [optional] |
|**idField** | **String** | The field in the Cloud Storage and BigQuery sources that indicates the unique IDs of the documents. For GcsSource it is the key of the JSON field. For instance, &#x60;my_id&#x60; for JSON &#x60;{\&quot;my_id\&quot;: \&quot;some_uuid\&quot;}&#x60;. For BigQuerySource it is the column name of the BigQuery table where the unique ids are stored. The values of the JSON field or the BigQuery column are used as the Document.ids. The JSON field or the BigQuery column must be of string type, and the values must be set as valid strings conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) with 1-63 characters. Otherwise, documents without valid IDs fail to be imported. Only set this field when using GcsSource or BigQuerySource, and when GcsSource.data_schema or BigQuerySource.data_schema is &#x60;custom&#x60;. And only set this field when auto_generate_ids is unset or set as &#x60;false&#x60;. Otherwise, an INVALID_ARGUMENT error is thrown. If it is unset, a default value &#x60;_id&#x60; is used when importing from the allowed data sources. |  [optional] |
|**inlineSource** | [**GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource**](GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource.md) |  |  [optional] |
|**reconciliationMode** | [**ReconciliationModeEnum**](#ReconciliationModeEnum) | The mode of reconciliation between existing documents and the documents to be imported. Defaults to ReconciliationMode.INCREMENTAL. |  [optional] |



## Enum: ReconciliationModeEnum

| Name | Value |
|---- | -----|
| RECONCILIATION_MODE_UNSPECIFIED | &quot;RECONCILIATION_MODE_UNSPECIFIED&quot; |
| INCREMENTAL | &quot;INCREMENTAL&quot; |
| FULL | &quot;FULL&quot; |



