

# CORSConfig

Experimental: Controls simple CORS responses for the associated domain. The configurable properties map closely to the CORS specification which should be referenced for a full discussion on their meaning: https://www.w3.org/TR/cors/ or https://developer.mozilla.org/docs/Web/HTTP/Access_control_CORS. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowCredentials** | **Boolean** | Indicates whether the response to request can be exposed when the omit credentials flag is unset https://www.w3.org/TR/cors/#access-control-allow-credentials-response-header.  |  [optional] |
|**allowedHeaders** | **List&lt;String&gt;** | Specifies what headers are allowed to be set when a request is made. https://www.w3.org/TR/cors/#access-control-allow-headers-response-header.  |  [optional] |
|**allowedMethods** | **List&lt;String&gt;** | Indicates which HTTP request types may be used to call an endpoint. https://www.w3.org/TR/cors/#access-control-allow-methods-response-header.  |  |
|**allowedOrigins** | **List&lt;String&gt;** | Must contain a single element specifying the domain (origin) allowed to make requsets to this domain. If any origin is acceptable &#39;*&#39; may be used as a wildcard https://www.w3.org/TR/cors/#origin-request-header, https://www.w3.org/TR/cors/#access-control-allow-origin-response-header.  |  |
|**exposedHeaders** | **List&lt;String&gt;** | Indicates which response headers may be accessed from the browser. https://www.w3.org/TR/cors/#http-access-control-expose-headers.  |  [optional] |
|**maxAge** | **Integer** | Sets how long (in seconds) the response to a preflight request may be cached. A value of -1 will disable caching. https://www.w3.org/TR/cors/#access-control-max-age-response-header.  |  [optional] |



