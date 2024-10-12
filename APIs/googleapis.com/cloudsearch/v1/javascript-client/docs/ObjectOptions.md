# CloudSearchApi.ObjectOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayOptions** | [**ObjectDisplayOptions**](ObjectDisplayOptions.md) |  | [optional] 
**freshnessOptions** | [**FreshnessOptions**](FreshnessOptions.md) |  | [optional] 
**suggestionFilteringOperators** | **[String]** | Operators that can be used to filter suggestions. For Suggest API, only operators mentioned here will be honored in the FilterOptions. Only TEXT and ENUM operators are supported. NOTE: \&quot;objecttype\&quot;, \&quot;type\&quot; and \&quot;mimetype\&quot; are already supported. This property is to configure schema specific operators. Even though this is an array, only one operator can be specified. This is an array for future extensibility. Operators mapping to multiple properties within the same object are not supported. If the operator spans across different object types, this option has to be set once for each object definition. | [optional] 


