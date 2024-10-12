

# SearchCatalogObjectsResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**latestTime** | **String** | When the associated product catalog was last updated. Will match the value for &#x60;end_time&#x60; or &#x60;cursor&#x60; if either field is included in the &#x60;SearchCatalog&#x60; request. |  [optional] |
|**objects** | [**List&lt;CatalogObject&gt;**](CatalogObject.md) | The CatalogObjects returned. |  [optional] |
|**relatedObjects** | [**List&lt;CatalogObject&gt;**](CatalogObject.md) | A list of CatalogObjects referenced by the objects in the &#x60;objects&#x60; field. |  [optional] |



