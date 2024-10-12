

# PaginationOptions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completed** | **Boolean** | Items filtered by whether they&#39;ve been fully watched or not.  Only available on the &#x60;/account/profile/watched/list&#x60; endpoint currently.  |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | Specific item type filter. |  [optional] |
|**maxRating** | **String** | The maximum rating (inclusive) of items returned, e.g. &#39;AUOFLC-PG&#39;. |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | The applied sort order if any. |  [optional] |
|**orderBy** | [**OrderByEnum**](#OrderByEnum) | The applied sort ordering property if any. |  [optional] |
|**pageSize** | **Integer** | The number of items to return in a list page. |  [optional] |



## Enum: ItemTypeEnum

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



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| ASC | &quot;asc&quot; |
| DESC | &quot;desc&quot; |



## Enum: OrderByEnum

| Name | Value |
|---- | -----|
| A_Z | &quot;a-z&quot; |
| RELEASE_YEAR | &quot;release-year&quot; |
| DATE_ADDED | &quot;date-added&quot; |



