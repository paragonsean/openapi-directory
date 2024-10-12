

# HttpRouteCorsPolicy

The Specification for allowing client side cross-origin requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowCredentials** | **Boolean** | In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access-Control-Allow-Credentials header. Default value is false. |  [optional] |
|**allowHeaders** | **List&lt;String&gt;** | Specifies the content for Access-Control-Allow-Headers header. |  [optional] |
|**allowMethods** | **List&lt;String&gt;** | Specifies the content for Access-Control-Allow-Methods header. |  [optional] |
|**allowOriginRegexes** | **List&lt;String&gt;** | Specifies the regular expression patterns that match allowed origins. For regular expression grammar, please see https://github.com/google/re2/wiki/Syntax. |  [optional] |
|**allowOrigins** | **List&lt;String&gt;** | Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either an item in allow_origins or an item in allow_origin_regexes. |  [optional] |
|**disabled** | **Boolean** | If true, the CORS policy is disabled. The default value is false, which indicates that the CORS policy is in effect. |  [optional] |
|**exposeHeaders** | **List&lt;String&gt;** | Specifies the content for Access-Control-Expose-Headers header. |  [optional] |
|**maxAge** | **String** | Specifies how long result of a preflight request can be cached in seconds. This translates to the Access-Control-Max-Age header. |  [optional] |



