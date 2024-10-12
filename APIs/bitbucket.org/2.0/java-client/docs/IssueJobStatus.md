

# IssueJobStatus

The status of an import or export job

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The total number of issues already imported/exported |  [optional] |
|**pct** | **BigDecimal** | The percentage of issues already imported/exported |  [optional] |
|**phase** | **String** | The phase of the import/export job |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the import/export job |  [optional] |
|**total** | **Integer** | The total number of issues being imported/exported |  [optional] |
|**type** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;ACCEPTED&quot; |
| STARTED | &quot;STARTED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILURE | &quot;FAILURE&quot; |



