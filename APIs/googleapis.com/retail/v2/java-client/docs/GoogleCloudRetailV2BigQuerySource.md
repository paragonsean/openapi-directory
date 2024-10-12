

# GoogleCloudRetailV2BigQuerySource

BigQuery source import data from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSchema** | **String** | The schema to use when parsing the data from the source. Supported values for product imports: * &#x60;product&#x60; (default): One JSON Product per line. Each product must have a valid Product.id. * &#x60;product_merchant_center&#x60;: See [Importing catalog data from Merchant Center](https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog#mc). Supported values for user events imports: * &#x60;user_event&#x60; (default): One JSON UserEvent per line. * &#x60;user_event_ga360&#x60;: The schema is available here: https://support.google.com/analytics/answer/3437719. * &#x60;user_event_ga4&#x60;: The schema is available here: https://support.google.com/analytics/answer/7029846. Supported values for autocomplete imports: * &#x60;suggestions&#x60; (default): One JSON completion suggestion per line. * &#x60;denylist&#x60;: One JSON deny suggestion per line. * &#x60;allowlist&#x60;: One JSON allow suggestion per line. |  [optional] |
|**datasetId** | **String** | Required. The BigQuery data set to copy the data from with a length limit of 1,024 characters. |  [optional] |
|**gcsStagingDir** | **String** | Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the BigQuery export to a specific Cloud Storage directory. |  [optional] |
|**partitionDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**projectId** | **String** | The project ID (can be project # or ID) that the BigQuery source is in with a length limit of 128 characters. If not specified, inherits the project ID from the parent request. |  [optional] |
|**tableId** | **String** | Required. The BigQuery table to copy the data from with a length limit of 1,024 characters. |  [optional] |



