# GooglePlayGameServices.EventUpdateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchFailures** | [**[EventBatchRecordFailure]**](EventBatchRecordFailure.md) | Any batch-wide failures which occurred applying updates. | [optional] 
**eventFailures** | [**[EventRecordFailure]**](EventRecordFailure.md) | Any failures updating a particular event. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventUpdateResponse&#x60;. | [optional] 
**playerEvents** | [**[PlayerEvent]**](PlayerEvent.md) | The current status of any updated events | [optional] 


