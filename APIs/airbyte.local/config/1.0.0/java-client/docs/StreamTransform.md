

# StreamTransform


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamDescriptor** | [**StreamDescriptor**](StreamDescriptor.md) |  |  |
|**transformType** | [**TransformTypeEnum**](#TransformTypeEnum) |  |  |
|**updateStream** | [**List&lt;FieldTransform&gt;**](FieldTransform.md) | list of field transformations. order does not matter. |  [optional] |



## Enum: TransformTypeEnum

| Name | Value |
|---- | -----|
| ADD_STREAM | &quot;add_stream&quot; |
| REMOVE_STREAM | &quot;remove_stream&quot; |
| UPDATE_STREAM | &quot;update_stream&quot; |



