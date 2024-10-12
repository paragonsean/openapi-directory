# DialogflowApi.GoogleCloudDialogflowCxV3WebhookGenericWebService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedCaCerts** | **[Blob]** | Optional. Specifies a list of allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, Dialogflow will use Google&#39;s default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with \&quot;subject alt name\&quot;. For instance a certificate can be self-signed using the following command, &#x60;&#x60;&#x60; openssl x509 -req -days 200 -in example.com.csr \\ -signkey example.com.key \\ -out example.com.crt \\ -extfile &lt;(printf \&quot;\\nsubjectAltName&#x3D;&#39;DNS:www.example.com&#39;\&quot;) &#x60;&#x60;&#x60; | [optional] 
**httpMethod** | **String** | Optional. HTTP method for the flexible webhook calls. Standard webhook always uses POST. | [optional] 
**parameterMapping** | **{String: String}** | Optional. Maps the values extracted from specific fields of the flexible webhook response into session parameters. - Key: session parameter name - Value: field path in the webhook response | [optional] 
**password** | **String** | The password for HTTP Basic authentication. | [optional] 
**requestBody** | **String** | Optional. Defines a custom JSON object as request body to send to flexible webhook. | [optional] 
**requestHeaders** | **{String: String}** | The HTTP request headers to send together with webhook requests. | [optional] 
**uri** | **String** | Required. The webhook URI for receiving POST requests. It must use https protocol. | [optional] 
**username** | **String** | The user name for HTTP Basic authentication. | [optional] 
**webhookType** | **String** | Optional. Type of the webhook. | [optional] 



## Enum: HttpMethodEnum


* `HTTP_METHOD_UNSPECIFIED` (value: `"HTTP_METHOD_UNSPECIFIED"`)

* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)

* `PATCH` (value: `"PATCH"`)

* `OPTIONS` (value: `"OPTIONS"`)





## Enum: WebhookTypeEnum


* `WEBHOOK_TYPE_UNSPECIFIED` (value: `"WEBHOOK_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `FLEXIBLE` (value: `"FLEXIBLE"`)




