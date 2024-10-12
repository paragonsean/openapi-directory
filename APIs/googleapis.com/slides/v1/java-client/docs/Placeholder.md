

# Placeholder

The placeholder information that uniquely identifies a placeholder shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**index** | **Integer** | The index of the placeholder. If the same placeholder types are present in the same page, they would have different index values. |  [optional] |
|**parentObjectId** | **String** | The object ID of this shape&#39;s parent placeholder. If unset, the parent placeholder shape does not exist, so the shape does not inherit properties from any other shape. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the placeholder. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| BODY | &quot;BODY&quot; |
| CHART | &quot;CHART&quot; |
| CLIP_ART | &quot;CLIP_ART&quot; |
| CENTERED_TITLE | &quot;CENTERED_TITLE&quot; |
| DIAGRAM | &quot;DIAGRAM&quot; |
| DATE_AND_TIME | &quot;DATE_AND_TIME&quot; |
| FOOTER | &quot;FOOTER&quot; |
| HEADER | &quot;HEADER&quot; |
| MEDIA | &quot;MEDIA&quot; |
| OBJECT | &quot;OBJECT&quot; |
| PICTURE | &quot;PICTURE&quot; |
| SLIDE_NUMBER | &quot;SLIDE_NUMBER&quot; |
| SUBTITLE | &quot;SUBTITLE&quot; |
| TABLE | &quot;TABLE&quot; |
| TITLE | &quot;TITLE&quot; |
| SLIDE_IMAGE | &quot;SLIDE_IMAGE&quot; |



