

# HtmlOperatorOptions

Used to provide a search operator for html properties. This is optional. Search operators let users restrict the query to specific fields relevant to the type of item being searched.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operatorName** | **String** | Indicates the operator name required in the query in order to isolate the html property. For example, if operatorName is *subject* and the property&#39;s name is *subjectLine*, then queries like *subject:&lt;value&gt;* show results only where the value of the property named *subjectLine* matches *&lt;value&gt;*. By contrast, a search that uses the same *&lt;value&gt;* without an operator return all items where *&lt;value&gt;* matches the value of any html properties or text within the content field for the item. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. |  [optional] |



