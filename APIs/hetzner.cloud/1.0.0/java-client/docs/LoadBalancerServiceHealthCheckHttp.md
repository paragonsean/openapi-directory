

# LoadBalancerServiceHealthCheckHttp

Additional configuration for protocol http

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** | Host header to send in the HTTP request. May not contain spaces, percent or backslash symbols. Can be null, in that case no host header is sent. |  |
|**path** | **String** | HTTP path to use for health checks. May not contain literal spaces, use percent-encoding instead. |  |
|**response** | **String** | String that must be contained in HTTP response in order to pass the health check |  [optional] |
|**statusCodes** | **List&lt;String&gt;** | List of returned HTTP status codes in order to pass the health check. Supports the wildcards &#x60;?&#x60; for exactly one character and &#x60;*&#x60; for multiple ones. The default is to pass the health check for any status code between 2?? and 3??. |  [optional] |
|**tls** | **Boolean** | Use HTTPS for health check |  [optional] |



