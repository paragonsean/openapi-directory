

# UpdateTableCellPropertiesRequest

Update the properties of a TableCell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableCellProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the table cell background solid fill color, set &#x60;fields&#x60; to &#x60;\&quot;tableCellBackgroundFill.solidFill.color\&quot;&#x60;. To reset a property to its default value, include its field name in the field mask but leave the field itself unset. |  [optional] |
|**objectId** | **String** | The object ID of the table. |  [optional] |
|**tableCellProperties** | [**TableCellProperties**](TableCellProperties.md) |  |  [optional] |
|**tableRange** | [**TableRange**](TableRange.md) |  |  [optional] |



