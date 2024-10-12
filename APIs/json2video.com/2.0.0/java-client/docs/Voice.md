

# Voice

Creates a voice audio element from the provided text

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cache** | **Boolean** | Element&#39;s cache policy. When true, the cached version (if exists) is used. When false, the assets is downloaded. |  [optional] |
|**comment** | **String** | Used for adding your comments |  [optional] |
|**duration** | **Float** | Element&#39;s duration in seconds. A value of -1 auto calculates the duration based on the asset intrinsic length or the scene duration. |  [optional] |
|**extraTime** | **Float** | Element&#39;s time span added after the playback. |  [optional] |
|**fadeIn** | **Float** | Adds a fade in effect to the element. Value in seconds. |  [optional] |
|**fadeOut** | **Float** | Adds a fade out effect to the element. Value in seconds. |  [optional] |
|**start** | **Float** | Element&#39;s starting time in seconds relative to the container scene or the movie if the element is in the Movie&#39;s elements array. |  [optional] |
|**zIndex** | **BigDecimal** | Element&#39;s z-index. Use this property to reorganize the layering of the elements like in HTML |  [optional] |
|**muted** | **Boolean** | Mutes the audio |  [optional] |
|**volume** | **BigDecimal** |  |  [optional] |
|**text** | **String** | The sentence or sentences to be converted to voice audio |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**voice** | **String** | The voice name to be used. Check &lt;a href&#x3D;\&quot;/docs/tutorial/voice-elements/\&quot;&gt;available voices&lt;/a&gt;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VOICE | &quot;voice&quot; |



