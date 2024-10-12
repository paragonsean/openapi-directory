

# IntegerOperatorOptions

Used to provide a search operator for integer properties. This is optional. Search operators let users restrict the query to specific fields relevant to the type of item being searched.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**greaterThanOperatorName** | **String** | Indicates the operator name required in the query in order to isolate the integer property using the greater-than operator. For example, if greaterThanOperatorName is *priorityabove* and the property&#39;s name is *priorityVal*, then queries like *priorityabove:&lt;value&gt;* show results only where the value of the property named *priorityVal* is greater than *&lt;value&gt;*. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. |  [optional] |
|**lessThanOperatorName** | **String** | Indicates the operator name required in the query in order to isolate the integer property using the less-than operator. For example, if lessThanOperatorName is *prioritybelow* and the property&#39;s name is *priorityVal*, then queries like *prioritybelow:&lt;value&gt;* show results only where the value of the property named *priorityVal* is less than *&lt;value&gt;*. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. |  [optional] |
|**operatorName** | **String** | Indicates the operator name required in the query in order to isolate the integer property. For example, if operatorName is *priority* and the property&#39;s name is *priorityVal*, then queries like *priority:&lt;value&gt;* show results only where the value of the property named *priorityVal* matches *&lt;value&gt;*. By contrast, a search that uses the same *&lt;value&gt;* without an operator returns all items where *&lt;value&gt;* matches the value of any String properties or text within the content field for the item. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. |  [optional] |



