

# ShapeProperties

The properties of a Shape. If the shape is a placeholder shape as determined by the placeholder field, then these properties may be inherited from a parent placeholder shape. Determining the rendered value of the property depends on the corresponding property_state field value. Any text autofit settings on the shape are automatically deactivated by requests that can impact how text fits in the shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autofit** | [**Autofit**](Autofit.md) |  |  [optional] |
|**contentAlignment** | [**ContentAlignmentEnum**](#ContentAlignmentEnum) | The alignment of the content in the shape. If unspecified, the alignment is inherited from a parent placeholder if it exists. If the shape has no parent, the default alignment matches the alignment for new shapes created in the Slides editor. |  [optional] |
|**link** | [**Link**](Link.md) |  |  [optional] |
|**outline** | [**Outline**](Outline.md) |  |  [optional] |
|**shadow** | [**Shadow**](Shadow.md) |  |  [optional] |
|**shapeBackgroundFill** | [**ShapeBackgroundFill**](ShapeBackgroundFill.md) |  |  [optional] |



## Enum: ContentAlignmentEnum

| Name | Value |
|---- | -----|
| CONTENT_ALIGNMENT_UNSPECIFIED | &quot;CONTENT_ALIGNMENT_UNSPECIFIED&quot; |
| CONTENT_ALIGNMENT_UNSUPPORTED | &quot;CONTENT_ALIGNMENT_UNSUPPORTED&quot; |
| TOP | &quot;TOP&quot; |
| MIDDLE | &quot;MIDDLE&quot; |
| BOTTOM | &quot;BOTTOM&quot; |



