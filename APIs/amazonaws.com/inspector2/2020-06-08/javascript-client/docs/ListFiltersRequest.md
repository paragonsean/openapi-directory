# Inspector2.ListFiltersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action the filter applies to matched findings. | [optional] 
**arns** | **[String]** | The Amazon resource number (ARN) of the filter. | [optional] 
**maxResults** | **Number** | The maximum number of results to return in the response. | [optional] 
**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 



## Enum: ActionEnum


* `NONE` (value: `"NONE"`)

* `SUPPRESS` (value: `"SUPPRESS"`)




