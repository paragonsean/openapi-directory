# Netatmo.NAWelcomeEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cameraId** | **String** | Camera that detected the event | [optional] 
**category** | **String** | Type of the detected object. | [optional] 
**eventList** | [**[NAWelcomeSubEvent]**](NAWelcomeSubEvent.md) |  | [optional] 
**id** | **String** | Identifier of the event | [optional] 
**isArrival** | **Boolean** | If person was considered away before being seen during this event | [optional] 
**message** | **String** | User facing event description | [optional] 
**personId** | **String** | Id of the person the event is about (if any) | [optional] 
**snapshot** | [**NAWelcomeSnapshot**](NAWelcomeSnapshot.md) |  | [optional] 
**subType** | **Number** | Subtypes of SD and Alim events. Go to Welcome page for further details. | [optional] 
**time** | **Number** | Time of occurence of event | [optional] 
**type** | **String** | Type of events. Go to the Welcome page for further details. | [optional] 
**videoId** | **String** | Identifier of the video | [optional] 
**videoStatus** | **String** | Status of the video (recording, deleted or available) | [optional] 



## Enum: CategoryEnum


* `human` (value: `"human"`)

* `animal` (value: `"animal"`)

* `vehicle` (value: `"vehicle"`)




