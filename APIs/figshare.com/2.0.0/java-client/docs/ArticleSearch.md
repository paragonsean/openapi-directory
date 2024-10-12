

# ArticleSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doi** | **String** | Only return articles with this doi |  [optional] |
|**handle** | **String** | Only return articles with this handle |  [optional] |
|**itemType** | **Long** | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | The field by which to order |  [optional] |
|**projectId** | **Long** | Only return articles in this project |  [optional] |
|**resourceDoi** | **String** | Only return articles with this resource_doi |  [optional] |
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
| DOWNLOADS | &quot;downloads&quot; |
| CITES | &quot;cites&quot; |



## Enum: OrderDirectionEnum

| Name | Value |
|---- | -----|
| ASC | &quot;asc&quot; |
| DESC | &quot;desc&quot; |



