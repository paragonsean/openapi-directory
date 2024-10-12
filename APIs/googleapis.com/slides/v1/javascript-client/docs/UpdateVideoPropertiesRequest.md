# GoogleSlidesApi.UpdateVideoPropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;videoProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the video outline color, set &#x60;fields&#x60; to &#x60;\&quot;outline.outlineFill.solidFill.color\&quot;&#x60;. To reset a property to its default value, include its field name in the field mask but leave the field itself unset. | [optional] 
**objectId** | **String** | The object ID of the video the updates are applied to. | [optional] 
**videoProperties** | [**VideoProperties**](VideoProperties.md) |  | [optional] 


