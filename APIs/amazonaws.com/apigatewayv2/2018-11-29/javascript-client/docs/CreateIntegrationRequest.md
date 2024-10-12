# AmazonApiGatewayV2.CreateIntegrationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionId** | **String** | A string with a length between [1-1024]. | [optional] 
**connectionType** | **String** | Represents a connection type. | [optional] 
**contentHandlingStrategy** | **String** | Specifies how to handle response payload content type conversions. Supported only for WebSocket APIs. | [optional] 
**credentialsArn** | **String** | Represents an Amazon Resource Name (ARN). | [optional] 
**description** | **String** | A string with a length between [0-1024]. | [optional] 
**integrationMethod** | **String** | A string with a length between [1-64]. | [optional] 
**integrationSubtype** | **String** | A string with a length between [1-128]. | [optional] 
**integrationType** | **String** | Represents an API method integration type. | 
**integrationUri** | **String** | A string representation of a URI with a length between [1-2048]. | [optional] 
**passthroughBehavior** | **String** | Represents passthrough behavior for an integration response. Supported only for WebSocket APIs. | [optional] 
**payloadFormatVersion** | **String** | A string with a length between [1-64]. | [optional] 
**requestParameters** | **{String: String}** | &lt;p&gt;For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.&lt;replaceable&gt;{location}&lt;/replaceable&gt;.&lt;replaceable&gt;{name}&lt;/replaceable&gt;           , where              &lt;replaceable&gt;{location}&lt;/replaceable&gt;            is querystring, path, or header; and              &lt;replaceable&gt;{name}&lt;/replaceable&gt;            must be a valid and unique method request parameter name.&lt;/p&gt; &lt;p&gt;For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html\&quot;&gt;Working with AWS service integrations for HTTP APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For HTTP API integrations without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &amp;lt;action&amp;gt;:&amp;lt;header|querystring|path&amp;gt;.&amp;lt;location&amp;gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\&quot;&gt;Transforming API requests and responses&lt;/a&gt;.&lt;/p&gt; | [optional] 
**requestTemplates** | **{String: String}** | A mapping of identifier keys to templates. The value is an actual template script. The key is typically a SelectionKey which is chosen based on evaluating a selection expression. | [optional] 
**responseParameters** | **{String: Object}** | Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. | [optional] 
**templateSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. | [optional] 
**timeoutInMillis** | **Number** | An integer with a value between [50-30000]. | [optional] 
**tlsConfig** | [**CreateIntegrationRequestTlsConfig**](CreateIntegrationRequestTlsConfig.md) |  | [optional] 



## Enum: ConnectionTypeEnum


* `INTERNET` (value: `"INTERNET"`)

* `VPC_LINK` (value: `"VPC_LINK"`)





## Enum: ContentHandlingStrategyEnum


* `BINARY` (value: `"CONVERT_TO_BINARY"`)

* `TEXT` (value: `"CONVERT_TO_TEXT"`)





## Enum: IntegrationTypeEnum


* `AWS` (value: `"AWS"`)

* `HTTP` (value: `"HTTP"`)

* `MOCK` (value: `"MOCK"`)

* `HTTP_PROXY` (value: `"HTTP_PROXY"`)

* `AWS_PROXY` (value: `"AWS_PROXY"`)





## Enum: PassthroughBehaviorEnum


* `WHEN_NO_MATCH` (value: `"WHEN_NO_MATCH"`)

* `NEVER` (value: `"NEVER"`)

* `WHEN_NO_TEMPLATES` (value: `"WHEN_NO_TEMPLATES"`)




