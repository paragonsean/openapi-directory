

# AnalysisArchiveAddResult

The result of adding a single digest to the archive

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | Details on the status, e.g. the error message |  [optional] |
|**digest** | **String** | The image digest requested to be added |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the archive add operation. Typically either &#39;archived&#39; or &#39;error&#39; |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ARCHIVED | &quot;archived&quot; |
| ARCHIVING | &quot;archiving&quot; |
| ERROR | &quot;error&quot; |



