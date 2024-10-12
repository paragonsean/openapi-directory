

# Page

Represents a page with results returned by query operation. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | **List&lt;Object&gt;** | A list of returned items |  [optional] |
|**limit** | **Integer** | A maximum number of returned items. If items.size() &lt; limit assume no more items |  [optional] |
|**offset** | **Integer** | An offset from a start of paging source |  [optional] |
|**totalCount** | **Integer** | Total count of available results. -1 if unknown |  [optional] |



