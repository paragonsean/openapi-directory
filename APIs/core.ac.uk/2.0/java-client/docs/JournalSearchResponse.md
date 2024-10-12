

# JournalSearchResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;Journal&gt;**](Journal.md) | Search results |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status |  |
|**totalHits** | **Integer** | Total number of journals matching the search criteria |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| TOO_MANY_QUERIES | &quot;TOO_MANY_QUERIES&quot; |
| MISSING_PARAMETER | &quot;MISSING_PARAMETER&quot; |
| INVALID_PARAMETER | &quot;INVALID_PARAMETER&quot; |



