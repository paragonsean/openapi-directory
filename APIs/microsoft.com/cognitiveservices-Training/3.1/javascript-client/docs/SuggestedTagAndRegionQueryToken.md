# CustomVisionTrainingClient.SuggestedTagAndRegionQueryToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation** | **String** | Continuation Id for database pagination. Initially null but later used to paginate. | [optional] 
**maxCount** | **Number** | Maximum number of results you want to be returned in the response. | [optional] 
**session** | **String** | SessionId for database query. Initially set to null but later used to paginate. | [optional] 
**sortBy** | **String** | OrderBy. Ordering mechanism for your results. | [optional] 
**tagIds** | **[String]** | Existing TagIds in project to filter suggested tags on. | [optional] 
**threshold** | **Number** | Confidence threshold to filter suggested tags on. | [optional] 



## Enum: SortByEnum


* `UncertaintyAscending` (value: `"UncertaintyAscending"`)

* `UncertaintyDescending` (value: `"UncertaintyDescending"`)




