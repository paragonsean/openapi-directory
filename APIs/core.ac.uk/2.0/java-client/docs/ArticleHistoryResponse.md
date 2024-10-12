

# ArticleHistoryResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;RawRecordXml&gt;**](RawRecordXml.md) | List of article versions |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| NOT_FOUND | &quot;Not found&quot; |
| TOO_MANY_QUERIES | &quot;Too many queries&quot; |
| MISSING_PARAMETER | &quot;Missing parameter&quot; |
| INVALID_PARAMETER | &quot;Invalid parameter&quot; |
| PARAMETER_OUT_OF_BOUNDS | &quot;Parameter out of bounds&quot; |



