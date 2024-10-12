

# Consumer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedRequestCount** | **BigDecimal** |  |  [optional] [readonly] |
|**applicationId** | **String** | ID of your Apideck Application |  [optional] [readonly] |
|**connections** | [**List&lt;ConsumerConnection&gt;**](ConsumerConnection.md) |  |  [optional] [readonly] |
|**consumerId** | **String** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. |  |
|**created** | **String** |  |  [optional] [readonly] |
|**metadata** | [**ConsumerMetadata**](ConsumerMetadata.md) |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**requestCountUpdated** | **String** |  |  [optional] [readonly] |
|**requestCounts** | [**RequestCountAllocation**](RequestCountAllocation.md) |  |  [optional] |
|**services** | **List&lt;String&gt;** |  |  [optional] [readonly] |



