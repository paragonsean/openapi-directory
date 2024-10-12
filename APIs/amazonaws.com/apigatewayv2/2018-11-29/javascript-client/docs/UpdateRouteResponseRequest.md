# AmazonApiGatewayV2.UpdateRouteResponseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modelSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. | [optional] 
**responseModels** | **{String: String}** | The route models. | [optional] 
**responseParameters** | [**{String: ParameterConstraints}**](ParameterConstraints.md) | The route parameters. | [optional] 
**routeResponseKey** | **String** | After evaluating a selection expression, the result is compared against one or more selection keys to find a matching key. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for a list of expressions and each expression&#39;s associated selection key type. | [optional] 


