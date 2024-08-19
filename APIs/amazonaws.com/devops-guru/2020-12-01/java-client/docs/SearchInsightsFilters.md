

# SearchInsightsFilters

Specifies values used to filter responses when searching for insights. You can use a <code>ResourceCollection</code>, <code>ServiceCollection</code>, array of severities, and an array of status values. Each filter type contains one or more values to search for. If you specify multiple filter types, the filter types are joined with an <code>AND</code>, and the request returns only results that match all of the specified filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**severities** | [**List**](List.md) |  |  [optional] |
|**statuses** | [**List**](List.md) |  |  [optional] |
|**resourceCollection** | [**ResourceCollection**](ResourceCollection.md) |  |  [optional] |
|**serviceCollection** | [**SearchInsightsRequestFiltersServiceCollection**](SearchInsightsRequestFiltersServiceCollection.md) |  |  [optional] |



