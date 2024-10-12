

# SearchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterConditions** | **Map&lt;String, Object&gt;** | Channel filter conditions |  |
|**limit** | **Integer** | Number of messages to return |  [optional] |
|**messageFilterConditions** | **Map&lt;String, Object&gt;** | Message filter conditions |  [optional] |
|**next** | **String** | Pagination parameter. Cannot be used with non-zero offset. |  [optional] |
|**offset** | **Integer** | Pagination offset. Cannot be used with sort or next. |  [optional] |
|**query** | **String** | Search phrase |  [optional] |
|**sort** | [**List&lt;SortParam&gt;**](SortParam.md) | Sort parameters. Cannot be used with non-zero offset |  [optional] |



