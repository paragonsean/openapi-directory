# AmazonApiGatewayV2.CreateApiRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiKeySelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. | [optional] 
**corsConfiguration** | [**CreateApiRequestCorsConfiguration**](CreateApiRequestCorsConfiguration.md) |  | [optional] 
**credentialsArn** | **String** | Represents an Amazon Resource Name (ARN). | [optional] 
**description** | **String** | A string with a length between [0-1024]. | [optional] 
**disableSchemaValidation** | **Boolean** | Avoid validating models when creating a deployment. Supported only for WebSocket APIs. | [optional] 
**disableExecuteApiEndpoint** | **Boolean** | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint. | [optional] 
**name** | **String** | A string with a length between [1-128]. | 
**protocolType** | **String** | Represents a protocol type. | 
**routeKey** | **String** | After evaluating a selection expression, the result is compared against one or more selection keys to find a matching key. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for a list of expressions and each expression&#39;s associated selection key type. | [optional] 
**routeSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. | [optional] 
**tags** | **{String: String}** | Represents a collection of tags associated with the resource. | [optional] 
**target** | **String** | A string representation of a URI with a length between [1-2048]. | [optional] 
**version** | **String** | A string with a length between [1-64]. | [optional] 



## Enum: ProtocolTypeEnum


* `WEBSOCKET` (value: `"WEBSOCKET"`)

* `HTTP` (value: `"HTTP"`)




