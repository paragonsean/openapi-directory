

# PaginationEnvelope

An envelope for paginated response. When accessing a collection through a GET endpoint, the results are wrapped in this envelope which includes metadata about those results. Results are presented within a `data` array. See [Pagination](/docs/api/#pagination) for more information. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**page** | **Integer** | The current [page](/docs/api/#pagination). |  [optional] [readonly] |
|**pages** | **Integer** | The total number of [pages](/docs/api/#pagination). |  [optional] [readonly] |
|**results** | **Integer** | The total number of results. |  [optional] [readonly] |



