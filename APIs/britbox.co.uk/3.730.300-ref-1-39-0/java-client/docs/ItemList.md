

# ItemList

A pageable list of items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFields** | **Map&lt;String, Object&gt;** | A map of custom fields defined by a curator for a list. |  [optional] |
|**description** | **String** | A full description of this list. |  [optional] |
|**id** | **String** | The id of this list |  |
|**images** | **Map&lt;String, URI&gt;** |  |  [optional] |
|**itemTypes** | [**List&lt;ItemTypesEnum&gt;**](#List&lt;ItemTypesEnum&gt;) | The types of items in the list |  [optional] |
|**items** | [**List&lt;ItemSummary&gt;**](ItemSummary.md) | A list of items |  |
|**listData** | [**ListData**](ListData.md) |  |  [optional] |
|**paging** | [**Pagination**](Pagination.md) |  |  |
|**parameter** | **String** | If this list is parameterized, then this contains the parameter of the list in the format &#x60;name:value&#x60;. For example the Movies Genre list will take a parameter &#x60;genre&#x60; with a given value. e.g. &#x60;genre:action&#x60; or &#x60;genre:drama&#x60;. |  [optional] |
|**path** | **String** | The path of this list |  |
|**shortDescription** | **String** | A short description of this list. |  [optional] |
|**size** | **Integer** | The total size of the list |  |
|**tagline** | **String** | The tagline of the item. |  [optional] |
|**themes** | [**List&lt;Theme&gt;**](Theme.md) |  |  [optional] |
|**title** | **String** | The title of this list |  [optional] |



## Enum: List&lt;ItemTypesEnum&gt;

| Name | Value |
|---- | -----|
| MOVIE | &quot;movie&quot; |
| SHOW | &quot;show&quot; |
| SEASON | &quot;season&quot; |
| EPISODE | &quot;episode&quot; |
| PROGRAM | &quot;program&quot; |
| LINK | &quot;link&quot; |
| TRAILER | &quot;trailer&quot; |
| CHANNEL | &quot;channel&quot; |
| CUSTOM_ASSET | &quot;customAsset&quot; |



