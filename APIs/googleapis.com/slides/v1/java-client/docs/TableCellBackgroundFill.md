

# TableCellBackgroundFill

The table cell background fill.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**propertyState** | [**PropertyStateEnum**](#PropertyStateEnum) | The background fill property state. Updating the fill on a table cell will implicitly update this field to &#x60;RENDERED&#x60;, unless another value is specified in the same request. To have no fill on a table cell, set this field to &#x60;NOT_RENDERED&#x60;. In this case, any other fill fields set in the same request will be ignored. |  [optional] |
|**solidFill** | [**SolidFill**](SolidFill.md) |  |  [optional] |



## Enum: PropertyStateEnum

| Name | Value |
|---- | -----|
| RENDERED | &quot;RENDERED&quot; |
| NOT_RENDERED | &quot;NOT_RENDERED&quot; |
| INHERIT | &quot;INHERIT&quot; |



