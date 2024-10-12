# FigshareApi.PrivateArticleSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceId** | **String** | only return collections with this resource_id | [optional] 
**doi** | **String** | Only return articles with this doi | [optional] 
**handle** | **String** | Only return articles with this handle | [optional] 
**itemType** | **Number** | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] 
**order** | **String** | The field by which to order | [optional] [default to &#39;created_date&#39;]
**projectId** | **Number** | Only return articles in this project | [optional] 
**resourceDoi** | **String** | Only return articles with this resource_doi | [optional] 
**group** | **Number** | only return collections from this group | [optional] 
**institution** | **Number** | only return collections from this institution | [optional] 
**limit** | **Number** | Number of results included on a page. Used for pagination with query | [optional] 
**modifiedSince** | **String** | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
**offset** | **Number** | Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
**orderDirection** | **String** | Direction of ordering | [optional] [default to &#39;desc&#39;]
**page** | **Number** | Page number. Used for pagination with page_size | [optional] 
**pageSize** | **Number** | The number of results included on a page. Used for pagination with page | [optional] [default to 10]
**publishedSince** | **String** | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
**searchFor** | **String** | Search term | [optional] 



## Enum: OrderEnum


* `published_date` (value: `"published_date"`)

* `modified_date` (value: `"modified_date"`)

* `views` (value: `"views"`)

* `shares` (value: `"shares"`)

* `downloads` (value: `"downloads"`)

* `cites` (value: `"cites"`)





## Enum: OrderDirectionEnum


* `asc` (value: `"asc"`)

* `desc` (value: `"desc"`)




