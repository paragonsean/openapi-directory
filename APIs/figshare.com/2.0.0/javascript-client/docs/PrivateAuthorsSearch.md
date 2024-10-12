# FigshareApi.PrivateAuthorsSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupId** | **Number** | Return only authors in this group or subgroups of the group | [optional] 
**institutionId** | **Number** | Return only authors associated to this institution | [optional] 
**isActive** | **Boolean** | Return only active authors if True | [optional] 
**isPublic** | **Boolean** | Return only authors that have published items if True | [optional] 
**limit** | **Number** | Number of results included on a page. Used for pagination with query | [optional] 
**offset** | **Number** | Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
**orcid** | **String** | Orcid of author | [optional] 
**order** | **String** | The field by which to order. Default varies by endpoint/resource. | [optional] [default to &#39;published_date&#39;]
**orderDirection** | **String** | Direction of ordering | [optional] [default to &#39;desc&#39;]
**page** | **Number** | Page number. Used for pagination with page_size | [optional] 
**pageSize** | **Number** | The number of results included on a page. Used for pagination with page | [optional] [default to 10]
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




