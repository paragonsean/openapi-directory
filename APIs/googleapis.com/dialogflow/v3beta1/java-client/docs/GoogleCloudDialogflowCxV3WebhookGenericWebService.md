

# GoogleCloudDialogflowCxV3WebhookGenericWebService

Represents configuration for a generic web service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedCaCerts** | **List&lt;byte[]&gt;** | Optional. Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, Dialogflow will use Google&#39;s default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with \&quot;subject alt name\&quot;. For instance a certificate can be self-signed using the following command, &#x60;&#x60;&#x60; openssl x509 -req -days 200 -in example.com.csr \\ -signkey example.com.key \\ -out example.com.crt \\ -extfile &lt;(printf \&quot;\\nsubjectAltName&#x3D;&#39;DNS:www.example.com&#39;\&quot;) &#x60;&#x60;&#x60; |  [optional] |
|**httpMethod** | [**HttpMethodEnum**](#HttpMethodEnum) | Optional. HTTP method for the flexible webhook calls. Standard webhook always uses POST. |  [optional] |
|**parameterMapping** | **Map&lt;String, String&gt;** | Optional. Maps the values extracted from specific fields of the flexible webhook response into session parameters. - Key: session parameter name - Value: field path in the webhook response |  [optional] |
|**password** | **String** | The password for HTTP Basic authentication. |  [optional] |
|**requestBody** | **String** | Optional. Defines a custom JSON object as request body to send to flexible webhook. |  [optional] |
|**requestHeaders** | **Map&lt;String, String&gt;** | The HTTP request headers to send together with webhook requests. |  [optional] |
|**uri** | **String** | Required. The webhook URI for receiving POST requests. It must use https protocol. |  [optional] |
|**username** | **String** | The user name for HTTP Basic authentication. |  [optional] |
|**webhookType** | [**WebhookTypeEnum**](#WebhookTypeEnum) | Optional. Type of the webhook. |  [optional] |



## Enum: HttpMethodEnum

| Name | Value |
|---- | -----|
| HTTP_METHOD_UNSPECIFIED | &quot;HTTP_METHOD_UNSPECIFIED&quot; |
| POST | &quot;POST&quot; |
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |
| PATCH | &quot;PATCH&quot; |
| OPTIONS | &quot;OPTIONS&quot; |



## Enum: WebhookTypeEnum

| Name | Value |
|---- | -----|
| WEBHOOK_TYPE_UNSPECIFIED | &quot;WEBHOOK_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| FLEXIBLE | &quot;FLEXIBLE&quot; |



