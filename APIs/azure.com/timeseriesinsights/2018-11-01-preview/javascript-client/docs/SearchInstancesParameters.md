# TimeSeriesInsightsClient.SearchInstancesParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlights** | **Boolean** | Definition of highlighted search results or not. When it is set to &#39;true&#39;, the highlighted search results are returned. When it is set to &#39;false&#39;, the highlighted search results are not returned. Default is &#39;true&#39;. | [optional] 
**pageSize** | **Number** | Maximum number of instances expected in each page of the result. Defaults to 10 when not set. Ranges from 1 to 100. If there are results beyond the page size, the user can use the continuation token to fetch the next page. | [optional] 
**recursive** | **Boolean** | Definition of which instances are returned. When recursive is set to &#39;true&#39;, all instances that have the path that starts with path the path parameter are returned. When recursive is set to &#39;false&#39;, only instances that have the path that exactly matches the path parameter are returned. Using recursive search allows to implement search user experience, while using non-recursive search allows to implement navigation experience. Optional, default is &#39;true&#39;. | [optional] 
**sort** | [**InstancesSortParameter**](InstancesSortParameter.md) |  | [optional] 


