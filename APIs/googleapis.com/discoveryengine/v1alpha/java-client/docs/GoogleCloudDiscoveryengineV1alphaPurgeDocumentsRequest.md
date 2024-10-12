

# GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest

Request message for DocumentService.PurgeDocuments method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorConfig** | [**GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig**](GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig.md) |  |  [optional] |
|**filter** | **String** | Required. Filter matching documents to purge. Only currently supported value is &#x60;*&#x60; (all items). |  [optional] |
|**force** | **Boolean** | Actually performs the purge. If &#x60;force&#x60; is set to false, return the expected purge count without deleting any documents. |  [optional] |
|**gcsSource** | [**GoogleCloudDiscoveryengineV1alphaGcsSource**](GoogleCloudDiscoveryengineV1alphaGcsSource.md) |  |  [optional] |



