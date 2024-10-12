# RubrikRestApi.EventSummaryV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterId** | **String** | The serialized AfterId of the response, if any. | [optional] 
**eventInfo** | **String** | A string that contains all the information for this event. | 
**eventName** | **String** | The event name. | [optional] 
**eventSeriesId** | **String** | The ID of the event series that this event belongs to. | 
**eventSeverity** | [**EventSeverityV1**](EventSeverityV1.md) |  | [optional] 
**eventStatus** | [**EventStatusV1**](EventStatusV1.md) |  | 
**eventType** | [**EventTypeV1**](EventTypeV1.md) |  | 
**id** | **String** | The event ID. | 
**jobInstanceId** | **String** | The ID of the associated job instance, if any. | [optional] 
**objectId** | **String** | The ID of the object associated with the event. | [optional] 
**objectName** | **String** | The name of the object associated with the event. | [optional] 
**objectType** | [**ObjectTypeV1**](ObjectTypeV1.md) |  | 
**time** | **Date** | The time at which this event occurred. | 


