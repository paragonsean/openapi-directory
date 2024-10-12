# TurbineLabsApi.CORSConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowCredentials** | **Boolean** | Indicates whether the response to request can be exposed when the omit credentials flag is unset https://www.w3.org/TR/cors/#access-control-allow-credentials-response-header.  | [optional] 
**allowedHeaders** | **[String]** | Specifies what headers are allowed to be set when a request is made. https://www.w3.org/TR/cors/#access-control-allow-headers-response-header.  | [optional] 
**allowedMethods** | **[String]** | Indicates which HTTP request types may be used to call an endpoint. https://www.w3.org/TR/cors/#access-control-allow-methods-response-header.  | 
**allowedOrigins** | **[String]** | Must contain a single element specifying the domain (origin) allowed to make requsets to this domain. If any origin is acceptable &#39;*&#39; may be used as a wildcard https://www.w3.org/TR/cors/#origin-request-header, https://www.w3.org/TR/cors/#access-control-allow-origin-response-header.  | 
**exposedHeaders** | **[String]** | Indicates which response headers may be accessed from the browser. https://www.w3.org/TR/cors/#http-access-control-expose-headers.  | [optional] 
**maxAge** | **Number** | Sets how long (in seconds) the response to a preflight request may be cached. A value of -1 will disable caching. https://www.w3.org/TR/cors/#access-control-max-age-response-header.  | [optional] 


