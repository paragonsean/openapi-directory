# Inspector2.ListAccountPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | The maximum number of results to return in the response. | [optional] 
**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 
**service** | **String** | The service scan type to check permissions for. | [optional] 



## Enum: ServiceEnum


* `EC2` (value: `"EC2"`)

* `ECR` (value: `"ECR"`)

* `LAMBDA` (value: `"LAMBDA"`)




