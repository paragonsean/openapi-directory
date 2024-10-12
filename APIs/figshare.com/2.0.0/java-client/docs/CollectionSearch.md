

# CollectionSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doi** | **String** | Only return collections with this doi |  [optional] |
|**handle** | **String** | Only return collections with this handle |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | The field by which to order. |  [optional] |
|**resourceDoi** | **String** | Only return collections with this resource_doi |  [optional] |
|**group** | **Integer** | only return collections from this group |  [optional] |
|**institution** | **Integer** | only return collections from this institution |  [optional] |
|**limit** | **Long** | Number of results included on a page. Used for pagination with query |  [optional] |
|**modifiedSince** | **String** | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD |  [optional] |
|**offset** | **Long** | Where to start the listing(the offset of the first result). Used for pagination with limit |  [optional] |
|**orderDirection** | [**OrderDirectionEnum**](#OrderDirectionEnum) | Direction of ordering |  [optional] |
|**page** | **Long** | Page number. Used for pagination with page_size |  [optional] |
|**pageSize** | **Long** | The number of results included on a page. Used for pagination with page |  [optional] |
|**publishedSince** | **String** | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD |  [optional] |
|**searchFor** | **String** | Search term |  [optional] |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| PUBLISHED_DATE | &quot;published_date&quot; |
| MODIFIED_DATE | &quot;modified_date&quot; |
| VIEWS | &quot;views&quot; |
| SHARES | &quot;shares&quot; |
| CITES | &quot;cites&quot; |



## Enum: OrderDirectionEnum

| Name | Value |
|---- | -----|
| ASC | &quot;asc&quot; |
| DESC | &quot;desc&quot; |



