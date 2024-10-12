# FigshareApi.CommonSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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



## Enum: OrderDirectionEnum


* `asc` (value: `"asc"`)

* `desc` (value: `"desc"`)




