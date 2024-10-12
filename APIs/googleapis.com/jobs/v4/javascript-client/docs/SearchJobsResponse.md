# CloudTalentSolutionApi.SearchJobsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadenedQueryJobsCount** | **Number** | If query broadening is enabled, we may append additional results from the broadened query. This number indicates how many of the jobs returned in the jobs field are from the broadened query. These results are always at the end of the jobs list. In particular, a value of 0, or if the field isn&#39;t set, all the jobs in the jobs list are from the original (without broadening) query. If this field is non-zero, subsequent requests with offset after this result set should contain all broadened results. | [optional] 
**histogramQueryResults** | [**[HistogramQueryResult]**](HistogramQueryResult.md) | The histogram results that match with specified SearchJobsRequest.histogram_queries. | [optional] 
**locationFilters** | [**[Location]**](Location.md) | The location filters that the service applied to the specified query. If any filters are lat-lng based, the Location.location_type is Location.LocationType.LOCATION_TYPE_UNSPECIFIED. | [optional] 
**matchingJobs** | [**[MatchingJob]**](MatchingJob.md) | The Job entities that match the specified SearchJobsRequest. | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**nextPageToken** | **String** | The token that specifies the starting position of the next page of results. This field is empty if there are no more results. | [optional] 
**spellCorrection** | [**SpellingCorrection**](SpellingCorrection.md) |  | [optional] 
**totalSize** | **Number** | Number of jobs that match the specified query. Note: This size is precise only if the total is less than 100,000. | [optional] 


