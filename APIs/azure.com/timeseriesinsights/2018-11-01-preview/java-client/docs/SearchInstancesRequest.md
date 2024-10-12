

# SearchInstancesRequest

Request to execute a search query against time series instances and return matching time series instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hierarchies** | [**SearchInstancesHierarchiesParameters**](SearchInstancesHierarchiesParameters.md) |  |  [optional] |
|**instances** | [**SearchInstancesParameters**](SearchInstancesParameters.md) |  |  [optional] |
|**path** | **List&lt;String&gt;** | Filter on hierarchy path of time series instances. Path is represented as array of string path segments. First element should be hierarchy name. Example: [\&quot;Location\&quot;, \&quot;California\&quot;]. Optional, case sensitive, never empty and can be null. |  [optional] |
|**searchString** | **String** | Query search string that will be matched to the attributes of time series instances. Example: \&quot;floor 100\&quot;. Case-insensitive, must be present, but can be empty string. |  |



