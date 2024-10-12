

# V2HttpRequest

A common proto for logging HTTP requests. Only contains semantics defined by the HTTP specification. Product-specific logging information MUST be defined in a separate message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheFillBytes** | **String** | The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted. |  [optional] |
|**cacheHit** | **Boolean** | Whether or not an entity was served from cache (with or without validation). |  [optional] |
|**cacheLookup** | **Boolean** | Whether or not a cache lookup was attempted. |  [optional] |
|**cacheValidatedWithOriginServer** | **Boolean** | Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if &#x60;cache_hit&#x60; is True. |  [optional] |
|**latency** | **String** | The request processing latency on the server, from the time the request was received until the response was sent. |  [optional] |
|**protocol** | **String** | Protocol used for the request. Examples: \&quot;HTTP/1.1\&quot;, \&quot;HTTP/2\&quot;, \&quot;websocket\&quot; |  [optional] |
|**referer** | **String** | The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). |  [optional] |
|**remoteIp** | **String** | The IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: &#x60;\&quot;192.168.1.1\&quot;&#x60;, &#x60;\&quot;FE80::0202:B3FF:FE1E:8329\&quot;&#x60;. |  [optional] |
|**requestMethod** | **String** | The request method. Examples: &#x60;\&quot;GET\&quot;&#x60;, &#x60;\&quot;HEAD\&quot;&#x60;, &#x60;\&quot;PUT\&quot;&#x60;, &#x60;\&quot;POST\&quot;&#x60;. |  [optional] |
|**requestSize** | **String** | The size of the HTTP request message in bytes, including the request headers and the request body. |  [optional] |
|**requestUrl** | **String** | The scheme (http, https), the host name, the path, and the query portion of the URL that was requested. Example: &#x60;\&quot;http://example.com/some/info?color&#x3D;red\&quot;&#x60;. |  [optional] |
|**responseSize** | **String** | The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body. |  [optional] |
|**serverIp** | **String** | The IP address (IPv4 or IPv6) of the origin server that the request was sent to. |  [optional] |
|**status** | **Integer** | The response code indicating the status of the response. Examples: 200, 404. |  [optional] |
|**userAgent** | **String** | The user agent sent by the client. Example: &#x60;\&quot;Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)\&quot;&#x60;. |  [optional] |



