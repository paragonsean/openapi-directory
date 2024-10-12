# PlatformApi.PresenceMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The event signified by a PresenceMessage. | [optional] [readonly] 
**clientId** | **String** | The client ID of the publisher of this presence update. | [optional] 
**connectionId** | **String** | The connection ID of the publisher of this presence update. | [optional] 
**data** | **String** | The presence update payload, if provided. | [optional] 
**encoding** | **String** | This will typically be empty as all presence updates received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload. | [optional] 
**extras** | [**Extras**](Extras.md) |  | [optional] 
**id** | **String** | Unique ID assigned by Ably to this presence update. | [optional] [readonly] 
**timestamp** | **Number** | Timestamp when the presence update was received by Ably, as milliseconds since the epoch. | [optional] [readonly] 



## Enum: ActionEnum


* `ABSENT` (value: `"ABSENT"`)

* `PRESENT` (value: `"PRESENT"`)

* `ENTER` (value: `"ENTER"`)

* `LEAVE` (value: `"LEAVE"`)

* `UPDATE` (value: `"UPDATE"`)




