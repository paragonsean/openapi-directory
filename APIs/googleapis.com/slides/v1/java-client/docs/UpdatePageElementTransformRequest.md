

# UpdatePageElementTransformRequest

Updates the transform of a page element. Updating the transform of a group will change the absolute transform of the page elements in that group, which can change their visual appearance. See the documentation for PageElement.transform for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applyMode** | [**ApplyModeEnum**](#ApplyModeEnum) | The apply mode of the transform update. |  [optional] |
|**objectId** | **String** | The object ID of the page element to update. |  [optional] |
|**transform** | [**AffineTransform**](AffineTransform.md) |  |  [optional] |



## Enum: ApplyModeEnum

| Name | Value |
|---- | -----|
| APPLY_MODE_UNSPECIFIED | &quot;APPLY_MODE_UNSPECIFIED&quot; |
| RELATIVE | &quot;RELATIVE&quot; |
| ABSOLUTE | &quot;ABSOLUTE&quot; |



