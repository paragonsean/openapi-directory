

# ProjectStatusBase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**title** | **String** | The title of the project status update. |  [optional] |
|**color** | [**ColorEnum**](#ColorEnum) | The color associated with the status update. |  |
|**htmlText** | **String** | [Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML. |  [optional] |
|**text** | **String** | The text content of the status update. |  |



## Enum: ColorEnum

| Name | Value |
|---- | -----|
| GREEN | &quot;green&quot; |
| YELLOW | &quot;yellow&quot; |
| RED | &quot;red&quot; |
| BLUE | &quot;blue&quot; |



