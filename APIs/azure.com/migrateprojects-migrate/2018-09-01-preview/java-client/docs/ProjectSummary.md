

# ProjectSummary

The project summary class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedSummary** | **Map&lt;String, String&gt;** | Gets or sets the extended summary. |  [optional] |
|**instanceType** | **String** | Gets the Instance type. |  [optional] [readonly] |
|**lastSummaryRefreshedTime** | **OffsetDateTime** | Gets or sets the time when summary was last refreshed. |  [optional] |
|**refreshSummaryState** | [**RefreshSummaryStateEnum**](#RefreshSummaryStateEnum) | Gets or sets the state of refresh summary. |  [optional] |



## Enum: RefreshSummaryStateEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;Started&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



