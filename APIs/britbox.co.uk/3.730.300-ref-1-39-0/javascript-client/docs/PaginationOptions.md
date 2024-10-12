# RocketServices.PaginationOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **Boolean** | Items filtered by whether they&#39;ve been fully watched or not.  Only available on the &#x60;/account/profile/watched/list&#x60; endpoint currently.  | [optional] 
**itemType** | **String** | Specific item type filter. | [optional] 
**maxRating** | **String** | The maximum rating (inclusive) of items returned, e.g. &#39;AUOFLC-PG&#39;. | [optional] 
**order** | **String** | The applied sort order if any. | [optional] 
**orderBy** | **String** | The applied sort ordering property if any. | [optional] 
**pageSize** | **Number** | The number of items to return in a list page. | [optional] 



## Enum: ItemTypeEnum


* `movie` (value: `"movie"`)

* `show` (value: `"show"`)

* `season` (value: `"season"`)

* `episode` (value: `"episode"`)

* `program` (value: `"program"`)

* `link` (value: `"link"`)

* `trailer` (value: `"trailer"`)

* `channel` (value: `"channel"`)

* `customAsset` (value: `"customAsset"`)





## Enum: OrderEnum


* `asc` (value: `"asc"`)

* `desc` (value: `"desc"`)





## Enum: OrderByEnum


* `a-z` (value: `"a-z"`)

* `release-year` (value: `"release-year"`)

* `date-added` (value: `"date-added"`)




