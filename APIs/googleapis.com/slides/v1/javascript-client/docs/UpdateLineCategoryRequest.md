# GoogleSlidesApi.UpdateLineCategoryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lineCategory** | **String** | The line category to update to. The exact line type is determined based on the category to update to and how it&#39;s routed to connect to other page elements. | [optional] 
**objectId** | **String** | The object ID of the line the update is applied to. Only a line with a category indicating it is a \&quot;connector\&quot; can be updated. The line may be rerouted after updating its category. | [optional] 



## Enum: LineCategoryEnum


* `LINE_CATEGORY_UNSPECIFIED` (value: `"LINE_CATEGORY_UNSPECIFIED"`)

* `STRAIGHT` (value: `"STRAIGHT"`)

* `BENT` (value: `"BENT"`)

* `CURVED` (value: `"CURVED"`)




