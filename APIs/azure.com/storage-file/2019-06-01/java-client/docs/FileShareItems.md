

# FileShareItems

Response schema. Contains list of shares returned, and if paging is requested or required, a URL to next page of shares.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | Request URL that can be used to query next page of shares. Returned when total number of requested shares exceed maximum page size. |  [optional] [readonly] |
|**value** | [**List&lt;FileShareItem&gt;**](FileShareItem.md) | List of file shares returned. |  [optional] [readonly] |



