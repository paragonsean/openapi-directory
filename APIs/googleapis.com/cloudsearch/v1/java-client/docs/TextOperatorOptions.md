

# TextOperatorOptions

Used to provide a search operator for text properties. This is optional. Search operators let users restrict the query to specific fields relevant to the type of item being searched.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exactMatchWithOperator** | **Boolean** | If true, the text value is tokenized as one atomic value in operator searches and facet matches. For example, if the operator name is \&quot;genre\&quot; and the value is \&quot;science-fiction\&quot; the query restrictions \&quot;genre:science\&quot; and \&quot;genre:fiction\&quot; doesn&#39;t match the item; \&quot;genre:science-fiction\&quot; does. Text value matching is case-sensitive and does not remove special characters. If false, the text is tokenized. For example, if the value is \&quot;science-fiction\&quot; the queries \&quot;genre:science\&quot; and \&quot;genre:fiction\&quot; matches the item. |  [optional] |
|**operatorName** | **String** | Indicates the operator name required in the query in order to isolate the text property. For example, if operatorName is *subject* and the property&#39;s name is *subjectLine*, then queries like *subject:&lt;value&gt;* show results only where the value of the property named *subjectLine* matches *&lt;value&gt;*. By contrast, a search that uses the same *&lt;value&gt;* without an operator returns all items where *&lt;value&gt;* matches the value of any text properties or text within the content field for the item. The operator name can only contain lowercase letters (a-z). The maximum length is 32 characters. |  [optional] |



