

# CatalogQuerySortedAttribute

The query expression to specify the key to sort search results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeName** | **String** | The attribute whose value is used as the sort key. |  |
|**initialAttributeValue** | **String** | The first attribute value to be returned by the query. Ascending sorts will return only objects with this value or greater, while descending sorts will return only objects with this value or less. If unset, start at the beginning (for ascending sorts) or end (for descending sorts). |  [optional] |
|**sortOrder** | **String** | The desired sort order, &#x60;\&quot;ASC\&quot;&#x60; (ascending) or &#x60;\&quot;DESC\&quot;&#x60; (descending). |  [optional] |



