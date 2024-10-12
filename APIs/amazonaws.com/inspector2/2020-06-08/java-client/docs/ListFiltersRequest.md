

# ListFiltersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The action the filter applies to matched findings. |  [optional] |
|**arns** | **List&lt;String&gt;** | The Amazon resource number (ARN) of the filter. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return in the response. |  [optional] |
|**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| SUPPRESS | &quot;SUPPRESS&quot; |



