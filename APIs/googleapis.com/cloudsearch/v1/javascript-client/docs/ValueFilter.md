# CloudSearchApi.ValueFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operatorName** | **String** | The &#x60;operator_name&#x60; applied to the query, such as *price_greater_than*. The filter can work against both types of filters defined in the schema for your data source: 1. &#x60;operator_name&#x60;, where the query filters results by the property that matches the value. 2. &#x60;greater_than_operator_name&#x60; or &#x60;less_than_operator_name&#x60; in your schema. The query filters the results for the property values that are greater than or less than the supplied value in the query. | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 


