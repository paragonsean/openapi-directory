

# PaginatedImageList

Pagination wrapped list of images that match some filter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPage** | **String** | True if additional pages exist (page + 1) or False if this is the last page |  [optional] |
|**page** | **String** | The page number returned (should match the requested page query string param) |  [optional] |
|**returnedCount** | **Integer** | The number of items sent in this response |  [optional] |
|**images** | [**List&lt;ImageWithPackages&gt;**](ImageWithPackages.md) |  |  [optional] |



