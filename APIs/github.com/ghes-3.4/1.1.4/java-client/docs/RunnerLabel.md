

# RunnerLabel

A label for a self hosted runner

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | Unique identifier of the label. |  [optional] |
|**name** | **String** | Name of the label. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of label. Read-only labels are applied automatically when the runner is configured. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| READ_ONLY | &quot;read-only&quot; |
| CUSTOM | &quot;custom&quot; |



