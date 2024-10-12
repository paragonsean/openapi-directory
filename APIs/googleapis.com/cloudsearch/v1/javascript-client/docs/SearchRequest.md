# CloudSearchApi.SearchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextAttributes** | [**[ContextAttribute]**](ContextAttribute.md) | Context attributes for the request which will be used to adjust ranking of search results. The maximum number of elements is 10. | [optional] 
**dataSourceRestrictions** | [**[DataSourceRestriction]**](DataSourceRestriction.md) | The sources to use for querying. If not specified, all data sources from the current search application are used. | [optional] 
**facetOptions** | [**[FacetOptions]**](FacetOptions.md) |  | [optional] 
**pageSize** | **Number** | Maximum number of search results to return in one page. Valid values are between 1 and 100, inclusive. Default value is 10. Minimum value is 50 when results beyond 2000 are requested. | [optional] 
**query** | **String** | The raw query string. See supported search operators in the [Narrow your search with operators](https://support.google.com/cloudsearch/answer/6172299) | [optional] 
**queryInterpretationOptions** | [**QueryInterpretationOptions**](QueryInterpretationOptions.md) |  | [optional] 
**requestOptions** | [**RequestOptions**](RequestOptions.md) |  | [optional] 
**sortOptions** | [**SortOptions**](SortOptions.md) |  | [optional] 
**start** | **Number** | Starting index of the results. | [optional] 


