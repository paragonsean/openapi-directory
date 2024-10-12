# NetBoxApi.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalHeaders** | **String** | User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format &lt;code&gt;Name: Value&lt;/code&gt;. Jinja2 template processing is supported with the same context as the request body (below). | [optional] 
**bodyTemplate** | **String** | Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: &lt;code&gt;event&lt;/code&gt;, &lt;code&gt;model&lt;/code&gt;, &lt;code&gt;timestamp&lt;/code&gt;, &lt;code&gt;username&lt;/code&gt;, &lt;code&gt;request_id&lt;/code&gt;, and &lt;code&gt;data&lt;/code&gt;. | [optional] 
**caFilePath** | **String** | The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults. | [optional] 
**conditions** | **Object** | A set of conditions which determine whether the webhook will be generated. | [optional] 
**contentTypes** | **[String]** |  | 
**created** | **Date** |  | [optional] [readonly] 
**display** | **String** |  | [optional] [readonly] 
**enabled** | **Boolean** |  | [optional] 
**httpContentType** | **String** | The complete list of official content types is available &lt;a href&#x3D;\&quot;https://www.iana.org/assignments/media-types/media-types.xhtml\&quot;&gt;here&lt;/a&gt;. | [optional] 
**httpMethod** | **String** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | 
**payloadUrl** | **String** | This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body. | 
**secret** | **String** | When provided, the request will include a &#39;X-Hook-Signature&#39; header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request. | [optional] 
**sslVerification** | **Boolean** | Enable SSL certificate verification. Disable with caution! | [optional] 
**typeCreate** | **Boolean** | Call this webhook when a matching object is created. | [optional] 
**typeDelete** | **Boolean** | Call this webhook when a matching object is deleted. | [optional] 
**typeUpdate** | **Boolean** | Call this webhook when a matching object is updated. | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: HttpMethodEnum


* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PUT` (value: `"PUT"`)

* `PATCH` (value: `"PATCH"`)

* `DELETE` (value: `"DELETE"`)




