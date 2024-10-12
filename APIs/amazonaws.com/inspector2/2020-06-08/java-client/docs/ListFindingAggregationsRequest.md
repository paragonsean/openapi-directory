

# ListFindingAggregationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | [**List&lt;StringFilter&gt;**](StringFilter.md) | The Amazon Web Services account IDs to retrieve finding aggregation data for. |  [optional] |
|**aggregationRequest** | [**ListFindingAggregationsRequestAggregationRequest**](ListFindingAggregationsRequestAggregationRequest.md) |  |  [optional] |
|**aggregationType** | [**AggregationTypeEnum**](#AggregationTypeEnum) | The type of the aggregation request. |  |
|**maxResults** | **Integer** | The maximum number of results to return in the response. |  [optional] |
|**nextToken** | **String** | A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the &lt;code&gt;NextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page. |  [optional] |



## Enum: AggregationTypeEnum

| Name | Value |
|---- | -----|
| FINDING_TYPE | &quot;FINDING_TYPE&quot; |
| PACKAGE | &quot;PACKAGE&quot; |
| TITLE | &quot;TITLE&quot; |
| REPOSITORY | &quot;REPOSITORY&quot; |
| AMI | &quot;AMI&quot; |
| AWS_EC2_INSTANCE | &quot;AWS_EC2_INSTANCE&quot; |
| AWS_ECR_CONTAINER | &quot;AWS_ECR_CONTAINER&quot; |
| IMAGE_LAYER | &quot;IMAGE_LAYER&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |
| AWS_LAMBDA_FUNCTION | &quot;AWS_LAMBDA_FUNCTION&quot; |
| LAMBDA_LAYER | &quot;LAMBDA_LAYER&quot; |



