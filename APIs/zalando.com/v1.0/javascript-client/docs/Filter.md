# ZalandoShop.Filter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiValue** | **Boolean** | can this filter be used multiple times with different values in one search request | 
**name** | **String** | The unique name for a filter | 
**type** | **String** | filter enum types | 
**values** | [**[FilterValue]**](FilterValue.md) | only if type is &#39;enum&#39; this list contains all possible filter values | 



## Enum: TypeEnum


* `SKU` (value: `"SKU"`)

* `KEY` (value: `"KEY"`)

* `ENUM` (value: `"ENUM"`)

* `STRING` (value: `"STRING"`)

* `RANGE` (value: `"RANGE"`)




