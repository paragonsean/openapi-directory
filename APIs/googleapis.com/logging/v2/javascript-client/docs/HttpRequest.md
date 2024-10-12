# CloudLoggingApi.HttpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheFillBytes** | **String** | The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted. | [optional] 
**cacheHit** | **Boolean** | Whether or not an entity was served from cache (with or without validation). | [optional] 
**cacheLookup** | **Boolean** | Whether or not a cache lookup was attempted. | [optional] 
**cacheValidatedWithOriginServer** | **Boolean** | Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if cache_hit is True. | [optional] 
**latency** | **String** | The request processing latency on the server, from the time the request was received until the response was sent. | [optional] 
**protocol** | **String** | Protocol used for the request. Examples: \&quot;HTTP/1.1\&quot;, \&quot;HTTP/2\&quot;, \&quot;websocket\&quot; | [optional] 
**referer** | **String** | The referer URL of the request, as defined in HTTP/1.1 Header Field Definitions (https://datatracker.ietf.org/doc/html/rfc2616#section-14.36). | [optional] 
**remoteIp** | **String** | The IP address (IPv4 or IPv6) of the client that issued the HTTP request. This field can include port information. Examples: \&quot;192.168.1.1\&quot;, \&quot;10.0.0.1:80\&quot;, \&quot;FE80::0202:B3FF:FE1E:8329\&quot;. | [optional] 
**requestMethod** | **String** | The request method. Examples: \&quot;GET\&quot;, \&quot;HEAD\&quot;, \&quot;PUT\&quot;, \&quot;POST\&quot;. | [optional] 
**requestSize** | **String** | The size of the HTTP request message in bytes, including the request headers and the request body. | [optional] 
**requestUrl** | **String** | The scheme (http, https), the host name, the path and the query portion of the URL that was requested. Example: \&quot;http://example.com/some/info?color&#x3D;red\&quot;. | [optional] 
**responseSize** | **String** | The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body. | [optional] 
**serverIp** | **String** | The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: \&quot;192.168.1.1\&quot;, \&quot;10.0.0.1:80\&quot;, \&quot;FE80::0202:B3FF:FE1E:8329\&quot;. | [optional] 
**status** | **Number** | The response code indicating the status of response. Examples: 200, 404. | [optional] 
**userAgent** | **String** | The user agent sent by the client. Example: \&quot;Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)\&quot;. | [optional] 


