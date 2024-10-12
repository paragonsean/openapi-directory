

# ListCatalogResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**objects** | [**List&lt;CatalogObject&gt;**](CatalogObject.md) | The CatalogObjects returned. |  [optional] |



