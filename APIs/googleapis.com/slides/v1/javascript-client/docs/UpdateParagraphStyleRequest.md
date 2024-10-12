# GoogleSlidesApi.UpdateParagraphStyleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cellLocation** | [**TableCellLocation**](TableCellLocation.md) |  | [optional] 
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;style&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example, to update the paragraph alignment, set &#x60;fields&#x60; to &#x60;\&quot;alignment\&quot;&#x60;. To reset a property to its default value, include its field name in the field mask but leave the field itself unset. | [optional] 
**objectId** | **String** | The object ID of the shape or table with the text to be styled. | [optional] 
**style** | [**ParagraphStyle**](ParagraphStyle.md) |  | [optional] 
**textRange** | [**Range**](Range.md) |  | [optional] 


