

# UpdateDataSourceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The new description for the data source. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The new data source type. |  |
|**serviceRoleArn** | **String** | The new service role Amazon Resource Name (ARN) for the data source. |  [optional] |
|**dynamodbConfig** | [**CreateDataSourceRequestDynamodbConfig**](CreateDataSourceRequestDynamodbConfig.md) |  |  [optional] |
|**lambdaConfig** | [**CreateDataSourceRequestLambdaConfig**](CreateDataSourceRequestLambdaConfig.md) |  |  [optional] |
|**elasticsearchConfig** | [**CreateDataSourceRequestElasticsearchConfig**](CreateDataSourceRequestElasticsearchConfig.md) |  |  [optional] |
|**openSearchServiceConfig** | [**CreateDataSourceRequestOpenSearchServiceConfig**](CreateDataSourceRequestOpenSearchServiceConfig.md) |  |  [optional] |
|**httpConfig** | [**CreateDataSourceRequestHttpConfig**](CreateDataSourceRequestHttpConfig.md) |  |  [optional] |
|**relationalDatabaseConfig** | [**CreateDataSourceRequestRelationalDatabaseConfig**](CreateDataSourceRequestRelationalDatabaseConfig.md) |  |  [optional] |
|**eventBridgeConfig** | [**CreateDataSourceRequestEventBridgeConfig**](CreateDataSourceRequestEventBridgeConfig.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AWS_LAMBDA | &quot;AWS_LAMBDA&quot; |
| AMAZON_DYNAMODB | &quot;AMAZON_DYNAMODB&quot; |
| AMAZON_ELASTICSEARCH | &quot;AMAZON_ELASTICSEARCH&quot; |
| NONE | &quot;NONE&quot; |
| HTTP | &quot;HTTP&quot; |
| RELATIONAL_DATABASE | &quot;RELATIONAL_DATABASE&quot; |
| AMAZON_OPENSEARCH_SERVICE | &quot;AMAZON_OPENSEARCH_SERVICE&quot; |
| AMAZON_EVENTBRIDGE | &quot;AMAZON_EVENTBRIDGE&quot; |



