# DataflowKitWebScraper.Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attrs** | **[String]** | A set of attributes to extract from a Field. Find more information about attributes | 
**details** | [**Parserequest**](Parserequest.md) | Details themself represent independent Parse request that extracts data from linked pages. | [optional] 
**filters** | [**[FieldFiltersInner]**](FieldFiltersInner.md) | Filters are used to pre-processing of text data when extracting. | [optional] 
**name** | **String** | Field name is used to aggregate results. | 
**selector** | **String** | Selector represents a CSS selector for data extraction within the given block. | 
**type** | **Number** | Selector type. ( 0 - image, 1 - text, 2 - link) | 



## Enum: [AttrsEnum]


* `text` (value: `"text"`)

* `href` (value: `"href"`)

* `src` (value: `"src"`)

* `alt` (value: `"alt"`)





## Enum: TypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)




