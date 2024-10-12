# CloudTasksApi.HttpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Blob** | HTTP request body. A request body is allowed only if the HTTP method is POST, PUT, or PATCH. It is an error to set body on a task with an incompatible HttpMethod. | [optional] 
**headers** | **{String: String}** | HTTP request headers. This map contains the header field names and values. Headers can be set when the task is created. These headers represent a subset of the headers that will accompany the task&#39;s HTTP request. Some HTTP request headers will be ignored or replaced. A partial list of headers that will be ignored or replaced is: * Any header that is prefixed with \&quot;X-CloudTasks-\&quot; will be treated as service header. Service headers define properties of the task and are predefined in CloudTask. * Host: This will be computed by Cloud Tasks and derived from HttpRequest.url. * Content-Length: This will be computed by Cloud Tasks. * User-Agent: This will be set to &#x60;\&quot;Google-Cloud-Tasks\&quot;&#x60;. * &#x60;X-Google-*&#x60;: Google use only. * &#x60;X-AppEngine-*&#x60;: Google use only. &#x60;Content-Type&#x60; won&#39;t be set by Cloud Tasks. You can explicitly set &#x60;Content-Type&#x60; to a media type when the task is created. For example, &#x60;Content-Type&#x60; can be set to &#x60;\&quot;application/octet-stream\&quot;&#x60; or &#x60;\&quot;application/json\&quot;&#x60;. Headers which can have multiple values (according to RFC2616) can be specified using comma-separated values. The size of the headers must be less than 80KB. | [optional] 
**httpMethod** | **String** | The HTTP method to use for the request. The default is POST. | [optional] 
**oauthToken** | [**OAuthToken**](OAuthToken.md) |  | [optional] 
**oidcToken** | [**OidcToken**](OidcToken.md) |  | [optional] 
**url** | **String** | Required. The full url path that the request will be sent to. This string must begin with either \&quot;http://\&quot; or \&quot;https://\&quot;. Some examples are: &#x60;http://acme.com&#x60; and &#x60;https://acme.com/sales:8080&#x60;. Cloud Tasks will encode some characters for safety and compatibility. The maximum allowed URL length is 2083 characters after encoding. The &#x60;Location&#x60; header response from a redirect response [&#x60;300&#x60; - &#x60;399&#x60;] may be followed. The redirect is not counted as a separate attempt. | [optional] 



## Enum: HttpMethodEnum


* `HTTP_METHOD_UNSPECIFIED` (value: `"HTTP_METHOD_UNSPECIFIED"`)

* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)

* `PATCH` (value: `"PATCH"`)

* `OPTIONS` (value: `"OPTIONS"`)




