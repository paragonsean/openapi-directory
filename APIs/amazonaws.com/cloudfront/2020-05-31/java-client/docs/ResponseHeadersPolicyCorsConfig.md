

# ResponseHeadersPolicyCorsConfig

<p>A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS). CloudFront adds these headers to HTTP responses that it sends for CORS requests that match a cache behavior associated with this response headers policy.</p> <p>For more information about CORS, see <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">Cross-Origin Resource Sharing (CORS)</a> in the MDN Web Docs.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControlAllowOrigins** | [**ResponseHeadersPolicyCorsConfigAccessControlAllowOrigins**](ResponseHeadersPolicyCorsConfigAccessControlAllowOrigins.md) |  |  |
|**accessControlAllowHeaders** | [**ResponseHeadersPolicyCorsConfigAccessControlAllowHeaders**](ResponseHeadersPolicyCorsConfigAccessControlAllowHeaders.md) |  |  |
|**accessControlAllowMethods** | [**ResponseHeadersPolicyCorsConfigAccessControlAllowMethods**](ResponseHeadersPolicyCorsConfigAccessControlAllowMethods.md) |  |  |
|**accessControlAllowCredentials** | [**Boolean**](Boolean.md) |  |  |
|**accessControlExposeHeaders** | [**ResponseHeadersPolicyCorsConfigAccessControlExposeHeaders**](ResponseHeadersPolicyCorsConfigAccessControlExposeHeaders.md) |  |  [optional] |
|**accessControlMaxAgeSec** | [**Integer**](Integer.md) |  |  [optional] |
|**originOverride** | [**Boolean**](Boolean.md) |  |  |



