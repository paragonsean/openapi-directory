# Inspector2.ListFindingAggregationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountIds** | [**[StringFilter]**](StringFilter.md) | The Amazon Web Services account IDs to retrieve finding aggregation data for. | [optional] 
**aggregationRequest** | [**ListFindingAggregationsRequestAggregationRequest**](ListFindingAggregationsRequestAggregationRequest.md) |  | [optional] 
**aggregationType** | **String** | The type of the aggregation request. | 
**maxResults** | **Number** | The maximum number of results to return in the response. | [optional] 
**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. | [optional] 



## Enum: AggregationTypeEnum


* `FINDING_TYPE` (value: `"FINDING_TYPE"`)

* `PACKAGE` (value: `"PACKAGE"`)

* `TITLE` (value: `"TITLE"`)

* `REPOSITORY` (value: `"REPOSITORY"`)

* `AMI` (value: `"AMI"`)

* `AWS_EC2_INSTANCE` (value: `"AWS_EC2_INSTANCE"`)

* `AWS_ECR_CONTAINER` (value: `"AWS_ECR_CONTAINER"`)

* `IMAGE_LAYER` (value: `"IMAGE_LAYER"`)

* `ACCOUNT` (value: `"ACCOUNT"`)

* `AWS_LAMBDA_FUNCTION` (value: `"AWS_LAMBDA_FUNCTION"`)

* `LAMBDA_LAYER` (value: `"LAMBDA_LAYER"`)




