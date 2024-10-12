# CloudSearchApi.DataSourceRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterOptions** | [**[FilterOptions]**](FilterOptions.md) | Filter options restricting the results. If multiple filters are present, they are grouped by object type before joining. Filters with the same object type are joined conjunctively, then the resulting expressions are joined disjunctively. The maximum number of elements is 20. NOTE: Suggest API supports only few filters at the moment: \&quot;objecttype\&quot;, \&quot;type\&quot; and \&quot;mimetype\&quot;. For now, schema specific filters cannot be used to filter suggestions. | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 


