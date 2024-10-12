

# CreateIntegrationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionId** | **String** | A string with a length between [1-1024]. |  [optional] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Represents a connection type. |  [optional] |
|**contentHandlingStrategy** | [**ContentHandlingStrategyEnum**](#ContentHandlingStrategyEnum) | Specifies how to handle response payload content type conversions. Supported only for WebSocket APIs. |  [optional] |
|**credentialsArn** | **String** | Represents an Amazon Resource Name (ARN). |  [optional] |
|**description** | **String** | A string with a length between [0-1024]. |  [optional] |
|**integrationMethod** | **String** | A string with a length between [1-64]. |  [optional] |
|**integrationSubtype** | **String** | A string with a length between [1-128]. |  [optional] |
|**integrationType** | [**IntegrationTypeEnum**](#IntegrationTypeEnum) | Represents an API method integration type. |  |
|**integrationUri** | **String** | A string representation of a URI with a length between [1-2048]. |  [optional] |
|**passthroughBehavior** | [**PassthroughBehaviorEnum**](#PassthroughBehaviorEnum) | Represents passthrough behavior for an integration response. Supported only for WebSocket APIs. |  [optional] |
|**payloadFormatVersion** | **String** | A string with a length between [1-64]. |  [optional] |
|**requestParameters** | **Map&lt;String, String&gt;** | &lt;p&gt;For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.&lt;replaceable&gt;{location}&lt;/replaceable&gt;.&lt;replaceable&gt;{name}&lt;/replaceable&gt;           , where              &lt;replaceable&gt;{location}&lt;/replaceable&gt;            is querystring, path, or header; and              &lt;replaceable&gt;{name}&lt;/replaceable&gt;            must be a valid and unique method request parameter name.&lt;/p&gt; &lt;p&gt;For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html\&quot;&gt;Working with AWS service integrations for HTTP APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For HTTP API integrations without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &amp;lt;action&amp;gt;:&amp;lt;header|querystring|path&amp;gt;.&amp;lt;location&amp;gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\&quot;&gt;Transforming API requests and responses&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**requestTemplates** | **Map&lt;String, String&gt;** | A mapping of identifier keys to templates. The value is an actual template script. The key is typically a SelectionKey which is chosen based on evaluating a selection expression. |  [optional] |
|**responseParameters** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. |  [optional] |
|**templateSelectionExpression** | **String** | An expression used to extract information at runtime. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\&quot;&gt;Selection Expressions&lt;/a&gt; for more information. |  [optional] |
|**timeoutInMillis** | **Integer** | An integer with a value between [50-30000]. |  [optional] |
|**tlsConfig** | [**CreateIntegrationRequestTlsConfig**](CreateIntegrationRequestTlsConfig.md) |  |  [optional] |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| INTERNET | &quot;INTERNET&quot; |
| VPC_LINK | &quot;VPC_LINK&quot; |



## Enum: ContentHandlingStrategyEnum

| Name | Value |
|---- | -----|
| BINARY | &quot;CONVERT_TO_BINARY&quot; |
| TEXT | &quot;CONVERT_TO_TEXT&quot; |



## Enum: IntegrationTypeEnum

| Name | Value |
|---- | -----|
| AWS | &quot;AWS&quot; |
| HTTP | &quot;HTTP&quot; |
| MOCK | &quot;MOCK&quot; |
| HTTP_PROXY | &quot;HTTP_PROXY&quot; |
| AWS_PROXY | &quot;AWS_PROXY&quot; |



## Enum: PassthroughBehaviorEnum

| Name | Value |
|---- | -----|
| WHEN_NO_MATCH | &quot;WHEN_NO_MATCH&quot; |
| NEVER | &quot;NEVER&quot; |
| WHEN_NO_TEMPLATES | &quot;WHEN_NO_TEMPLATES&quot; |



