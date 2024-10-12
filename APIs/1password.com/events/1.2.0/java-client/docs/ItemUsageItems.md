

# ItemUsageItems

An object wrapping cursor properties and a list of items usages

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | Cursor to fetch more data if available or continue the polling process if required |  [optional] |
|**hasMore** | **Boolean** | Whether there may still be more data to fetch using the returned cursor. If true, the subsequent request could still be empty. |  [optional] |
|**items** | [**List&lt;ItemUsage&gt;**](ItemUsage.md) |  |  [optional] |



