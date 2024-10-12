

# EventUpdateResponse

An event period update resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchFailures** | [**List&lt;EventBatchRecordFailure&gt;**](EventBatchRecordFailure.md) | Any batch-wide failures which occurred applying updates. |  [optional] |
|**eventFailures** | [**List&lt;EventRecordFailure&gt;**](EventRecordFailure.md) | Any failures updating a particular event. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventUpdateResponse&#x60;. |  [optional] |
|**playerEvents** | [**List&lt;PlayerEvent&gt;**](PlayerEvent.md) | The current status of any updated events |  [optional] |



