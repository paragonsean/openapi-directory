

# UpdateRouteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKeyRequired** | **Boolean** | Specifies whether an API key is required for the route. Supported only for WebSocket APIs. |  [optional] |
|**authorizationScopes** | **List&lt;String&gt;** | A list of authorization scopes configured on a route. The scopes are used with a JWT authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes. |  [optional] |
|**authorizationType** | [**AuthorizationTypeEnum**](#AuthorizationTypeEnum) | The authorization type. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer. For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer. |  [optional] |
|**authorizerId** | **String** | The identifier. |  [optional] |
|**modelSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. |  [optional] |
|**operationName** | **String** | A string with a length between [1-64]. |  [optional] |
|**requestModels** | **Map&lt;String, String&gt;** | The route models. |  [optional] |
|**requestParameters** | [**Map&lt;String, ParameterConstraints&gt;**](ParameterConstraints.md) | The route parameters. |  [optional] |
|**routeKey** | **String** | After evaluating a selection expression, the result is compared against one or more selection keys to find a matching key. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for a list of expressions and each expression&#39;s associated selection key type. |  [optional] |
|**routeResponseSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. |  [optional] |
|**target** | **String** | A string with a length between [1-128]. |  [optional] |



## Enum: AuthorizationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| AWS_IAM | &quot;AWS_IAM&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| JWT | &quot;JWT&quot; |



