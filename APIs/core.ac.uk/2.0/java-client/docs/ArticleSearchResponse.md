

# ArticleSearchResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;Article&gt;**](Article.md) | Search results |  |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status |  |
|**totalHits** | **Integer** | Total number of articles matching the search criteria |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| NOT_FOUND | &quot;Not found&quot; |
| TOO_MANY_QUERIES | &quot;Too many queries&quot; |
| MISSING_PARAMETER | &quot;Missing parameter&quot; |
| INVALID_PARAMETER | &quot;Invalid parameter&quot; |
| PARAMETER_OUT_OF_BOUNDS | &quot;Parameter out of bounds&quot; |



