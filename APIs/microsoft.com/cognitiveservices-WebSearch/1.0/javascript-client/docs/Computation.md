# WebSearchClient.Computation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **String** | The math or conversion expression. If the query contains a request to convert units of measure (for example, meters to feet), this field contains the from units and value contains the to units. If the query contains a mathematical expression such as 2+2, this field contains the expression and value contains the answer. Note that mathematical expressions may be normalized. For example, if the query was sqrt(4^2+8^2), the normalized expression may be sqrt((4^2)+(8^2)). If the user&#39;s query is a math question and the textDecorations query parameter is set to true, the expression string may include formatting markers. For example, if the user&#39;s query is log(2), the normalized expression includes the subscript markers. For more information, see Hit Highlighting. | 
**value** | **String** | The expression&#39;s answer. | 


