

# FieldTransform

A transformation of a field of the document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appendMissingElements** | [**ArrayValue**](ArrayValue.md) |  |  [optional] |
|**fieldPath** | **String** | The path of the field. See Document.fields for the field path syntax reference. |  [optional] |
|**increment** | [**Value**](Value.md) |  |  [optional] |
|**maximum** | [**Value**](Value.md) |  |  [optional] |
|**minimum** | [**Value**](Value.md) |  |  [optional] |
|**removeAllFromArray** | [**ArrayValue**](ArrayValue.md) |  |  [optional] |
|**setToServerValue** | [**SetToServerValueEnum**](#SetToServerValueEnum) | Sets the field to the given server value. |  [optional] |



## Enum: SetToServerValueEnum

| Name | Value |
|---- | -----|
| SERVER_VALUE_UNSPECIFIED | &quot;SERVER_VALUE_UNSPECIFIED&quot; |
| REQUEST_TIME | &quot;REQUEST_TIME&quot; |



