# TimeSeriesInsightsClient.SearchInstancesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchies** | [**SearchInstancesHierarchiesParameters**](SearchInstancesHierarchiesParameters.md) |  | [optional] 
**instances** | [**SearchInstancesParameters**](SearchInstancesParameters.md) |  | [optional] 
**path** | **[String]** | Filter on hierarchy path of time series instances. Path is represented as array of string path segments. First element should be hierarchy name. Example: [\&quot;Location\&quot;, \&quot;California\&quot;]. Optional, case sensitive, never empty and can be null. | [optional] 
**searchString** | **String** | Query search string that will be matched to the attributes of time series instances. Example: \&quot;floor 100\&quot;. Case-insensitive, must be present, but can be empty string. | 


