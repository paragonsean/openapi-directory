

# InvideoTiming

Describes a temporal position of a visual widget inside a video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**durationMs** | **String** | Defines the duration in milliseconds for which the promotion should be displayed. If missing, the client should use the default. |  [optional] |
|**offsetMs** | **String** | Defines the time at which the promotion will appear. Depending on the value of type the value of the offsetMs field will represent a time offset from the start or from the end of the video, expressed in milliseconds. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Describes a timing type. If the value is offsetFromStart, then the offsetMs field represents an offset from the start of the video. If the value is offsetFromEnd, then the offsetMs field represents an offset from the end of the video. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OFFSET_FROM_START | &quot;offsetFromStart&quot; |
| OFFSET_FROM_END | &quot;offsetFromEnd&quot; |



