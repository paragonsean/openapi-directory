# RocketServices.ItemList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for a list. | [optional] 
**description** | **String** | A full description of this list. | [optional] 
**id** | **String** | The id of this list | 
**images** | **{String: String}** |  | [optional] 
**itemTypes** | **[String]** | The types of items in the list | [optional] 
**items** | [**[ItemSummary]**](ItemSummary.md) | A list of items | 
**listData** | [**ListData**](ListData.md) |  | [optional] 
**paging** | [**Pagination**](Pagination.md) |  | 
**parameter** | **String** | If this list is parameterized, then this contains the parameter of the list in the format &#x60;name:value&#x60;. For example the Movies Genre list will take a parameter &#x60;genre&#x60; with a given value. e.g. &#x60;genre:action&#x60; or &#x60;genre:drama&#x60;. | [optional] 
**path** | **String** | The path of this list | 
**shortDescription** | **String** | A short description of this list. | [optional] 
**size** | **Number** | The total size of the list | 
**tagline** | **String** | The tagline of the item. | [optional] 
**themes** | [**[Theme]**](Theme.md) |  | [optional] 
**title** | **String** | The title of this list | [optional] 



## Enum: [ItemTypesEnum]


* `movie` (value: `"movie"`)

* `show` (value: `"show"`)

* `season` (value: `"season"`)

* `episode` (value: `"episode"`)

* `program` (value: `"program"`)

* `link` (value: `"link"`)

* `trailer` (value: `"trailer"`)

* `channel` (value: `"channel"`)

* `customAsset` (value: `"customAsset"`)




