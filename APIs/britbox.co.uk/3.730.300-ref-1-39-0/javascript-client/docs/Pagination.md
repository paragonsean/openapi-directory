# RocketServices.Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**PaginationAuth**](PaginationAuth.md) |  | [optional] 
**next** | **String** | Path to load next page of data, or null if not available | [optional] 
**options** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 
**page** | **Number** | The current page number.  A value of 0 indicates that the fist page has not yet been loaded. This is useful when wanting to return the paging metadata to indicate how to load in the first page.  | 
**previous** | **String** | Path to load previous page of data, or null if not available. | [optional] 
**size** | **Number** | The current page size.  A value of -1 indicates that the size has not yet been determined. This may arise when embedding secure list pagination info in a page which must be cached by a CDN. For example a Bookmarks list.  | [optional] 
**total** | **Number** | The total number of pages available given the current page size.  A value of -1 indicates that the total has not yet been determined. This may arise when embedding secure list pagination info in a page which must be cached by a CDN. For example a Bookmarks list.  | 


