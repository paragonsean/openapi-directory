# GoogleSlidesApi.UpdateTableBorderPropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borderPosition** | **String** | The border position in the table range the updates should apply to. If a border position is not specified, the updates will apply to all borders in the table range. | [optional] 
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableBorderProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the table border solid fill color, set &#x60;fields&#x60; to &#x60;\&quot;tableBorderFill.solidFill.color\&quot;&#x60;. To reset a property to its default value, include its field name in the field mask but leave the field itself unset. | [optional] 
**objectId** | **String** | The object ID of the table. | [optional] 
**tableBorderProperties** | [**TableBorderProperties**](TableBorderProperties.md) |  | [optional] 
**tableRange** | [**TableRange**](TableRange.md) |  | [optional] 



## Enum: BorderPositionEnum


* `ALL` (value: `"ALL"`)

* `BOTTOM` (value: `"BOTTOM"`)

* `INNER` (value: `"INNER"`)

* `INNER_HORIZONTAL` (value: `"INNER_HORIZONTAL"`)

* `INNER_VERTICAL` (value: `"INNER_VERTICAL"`)

* `LEFT` (value: `"LEFT"`)

* `OUTER` (value: `"OUTER"`)

* `RIGHT` (value: `"RIGHT"`)

* `TOP` (value: `"TOP"`)




