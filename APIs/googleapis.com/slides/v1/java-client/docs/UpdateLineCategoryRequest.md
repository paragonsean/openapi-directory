

# UpdateLineCategoryRequest

Updates the category of a line.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineCategory** | [**LineCategoryEnum**](#LineCategoryEnum) | The line category to update to. The exact line type is determined based on the category to update to and how it&#39;s routed to connect to other page elements. |  [optional] |
|**objectId** | **String** | The object ID of the line the update is applied to. Only a line with a category indicating it is a \&quot;connector\&quot; can be updated. The line may be rerouted after updating its category. |  [optional] |



## Enum: LineCategoryEnum

| Name | Value |
|---- | -----|
| LINE_CATEGORY_UNSPECIFIED | &quot;LINE_CATEGORY_UNSPECIFIED&quot; |
| STRAIGHT | &quot;STRAIGHT&quot; |
| BENT | &quot;BENT&quot; |
| CURVED | &quot;CURVED&quot; |



