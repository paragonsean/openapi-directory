# AmazonLexModelBuildingV2.SearchAssociatedTranscriptsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**searchOrder** | **String** | How SearchResults are ordered. Valid values are Ascending or Descending. The default is Descending. | [optional] 
**filters** | [**[AssociatedTranscriptFilter]**](AssociatedTranscriptFilter.md) | A list of filter objects. | 
**maxResults** | **Number** | The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned. | [optional] 
**nextIndex** | **Number** | If the response from the SearchAssociatedTranscriptsRequest operation contains more results than specified in the maxResults parameter, an index is returned in the response. Use that index in the nextIndex parameter to return the next page of results. | [optional] 



## Enum: SearchOrderEnum


* `Ascending` (value: `"Ascending"`)

* `Descending` (value: `"Descending"`)




