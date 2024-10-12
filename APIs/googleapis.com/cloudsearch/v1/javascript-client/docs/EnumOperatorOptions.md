# CloudSearchApi.EnumOperatorOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operatorName** | **String** | Indicates the operator name required in the query in order to isolate the enum property. For example, if operatorName is *priority* and the property&#39;s name is *priorityVal*, then queries like *priority:&lt;value&gt;* show results only where the value of the property named *priorityVal* matches *&lt;value&gt;*. By contrast, a search that uses the same *&lt;value&gt;* without an operator returns all items where *&lt;value&gt;* matches the value of any String properties or text within the content field for the item. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. | [optional] 


