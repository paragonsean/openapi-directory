

# NAWelcomeEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cameraId** | **String** | Camera that detected the event |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Type of the detected object. |  [optional] |
|**eventList** | [**List&lt;NAWelcomeSubEvent&gt;**](NAWelcomeSubEvent.md) |  |  [optional] |
|**id** | **String** | Identifier of the event |  [optional] |
|**isArrival** | **Boolean** | If person was considered away before being seen during this event |  [optional] |
|**message** | **String** | User facing event description |  [optional] |
|**personId** | **String** | Id of the person the event is about (if any) |  [optional] |
|**snapshot** | [**NAWelcomeSnapshot**](NAWelcomeSnapshot.md) |  |  [optional] |
|**subType** | **Integer** | Subtypes of SD and Alim events. Go to Welcome page for further details. |  [optional] |
|**time** | **Integer** | Time of occurence of event |  [optional] |
|**type** | **String** | Type of events. Go to the Welcome page for further details. |  [optional] |
|**videoId** | **String** | Identifier of the video |  [optional] |
|**videoStatus** | **String** | Status of the video (recording, deleted or available) |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| HUMAN | &quot;human&quot; |
| ANIMAL | &quot;animal&quot; |
| VEHICLE | &quot;vehicle&quot; |



