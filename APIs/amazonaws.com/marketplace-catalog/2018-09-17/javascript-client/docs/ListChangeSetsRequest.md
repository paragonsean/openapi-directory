# AwsMarketplaceCatalogService.ListChangeSetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **String** | The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;  | 
**filterList** | [**[Filter]**](Filter.md) | An array of filter objects. | [optional] 
**sort** | [**ListChangeSetsRequestSort**](ListChangeSetsRequestSort.md) |  | [optional] 
**maxResults** | **Number** | The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20. | [optional] 
**nextToken** | **String** | The token value retrieved from a previous call to access the next page of results. | [optional] 


