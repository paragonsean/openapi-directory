

# AccountsCustomBatchResponseEntry

A batch entry encoding a single non-batch accounts response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**batchId** | **Integer** | The ID of the request entry this entry responds to. |  [optional] |
|**errors** | [**Errors**](Errors.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#accountsCustomBatchResponseEntry&#x60;\&quot; |  [optional] |
|**linkStatus** | **String** | Deprecated. This field is never set. Acceptable values are: - \&quot;&#x60;active&#x60;\&quot; - \&quot;&#x60;inactive&#x60;\&quot; - \&quot;&#x60;pending&#x60;\&quot;  |  [optional] |



