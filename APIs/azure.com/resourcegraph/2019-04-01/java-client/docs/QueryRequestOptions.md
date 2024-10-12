

# QueryRequestOptions

The options for query evaluation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**$skip** | **Integer** | The number of rows to skip from the beginning of the results. Overrides the next page offset when &#x60;&#x60;&#x60;$skipToken&#x60;&#x60;&#x60; property is present. |  [optional] |
|**$skipToken** | **String** | Continuation token for pagination, capturing the next page size and offset, as well as the context of the query. |  [optional] |
|**$top** | **Integer** | The maximum number of rows that the query should return. Overrides the page size when &#x60;&#x60;&#x60;$skipToken&#x60;&#x60;&#x60; property is present. |  [optional] |
|**resultFormat** | [**ResultFormatEnum**](#ResultFormatEnum) | Defines in which format query result returned. |  [optional] |



## Enum: ResultFormatEnum

| Name | Value |
|---- | -----|
| TABLE | &quot;table&quot; |
| OBJECT_ARRAY | &quot;objectArray&quot; |



