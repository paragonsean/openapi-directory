

# EventSearchResponse

The result set for the specified event search criteria.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**events** | [**List&lt;Event&gt;**](Event.md) | A list of results that match the search criteria. |  [optional] |
|**href** | **String** | The relative path to the current set of results. |  [optional] |
|**limit** | **Integer** | The maximum number of items, from the current result set, returned on a single page. Default: 20 |  [optional] |
|**next** | **String** | The relative path to the next set of results. |  [optional] |
|**offset** | **Integer** | The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0 |  [optional] |
|**prev** | **String** | The relative path to the previous set of results. |  [optional] |
|**total** | **Integer** | The total number of matches for the specified search criteria. |  [optional] |



