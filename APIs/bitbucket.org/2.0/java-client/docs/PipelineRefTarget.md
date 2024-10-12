

# PipelineRefTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commit** | [**Commit**](Commit.md) |  |  [optional] |
|**refName** | **String** | The name of the reference. |  [optional] |
|**refType** | [**RefTypeEnum**](#RefTypeEnum) | The type of reference (branch/tag). |  [optional] |
|**selector** | [**PipelineSelector**](PipelineSelector.md) |  |  [optional] |



## Enum: RefTypeEnum

| Name | Value |
|---- | -----|
| BRANCH | &quot;branch&quot; |
| TAG | &quot;tag&quot; |
| NAMED_BRANCH | &quot;named_branch&quot; |
| BOOKMARK | &quot;bookmark&quot; |



