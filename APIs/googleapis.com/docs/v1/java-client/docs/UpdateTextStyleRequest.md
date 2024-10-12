

# UpdateTextStyleRequest

Update the styling of text.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;text_style&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example, to update the text style to bold, set &#x60;fields&#x60; to &#x60;\&quot;bold\&quot;&#x60;. To reset a property to its default value, include its field name in the field mask but leave the field itself unset. |  [optional] |
|**range** | [**Range**](Range.md) |  |  [optional] |
|**textStyle** | [**TextStyle**](TextStyle.md) |  |  [optional] |



