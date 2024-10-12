

# EndpointPropertiesUpdateParameters

The JSON object containing endpoint update parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentTypesToCompress** | **List&lt;String&gt;** | List of content types on which compression applies. The value should be a valid MIME type. |  [optional] |
|**defaultOriginGroup** | [**ResourceReference**](ResourceReference.md) |  |  [optional] |
|**deliveryPolicy** | [**EndpointPropertiesUpdateParametersDeliveryPolicy**](EndpointPropertiesUpdateParametersDeliveryPolicy.md) |  |  [optional] |
|**geoFilters** | [**List&lt;GeoFilter&gt;**](GeoFilter.md) | List of rules defining the user&#39;s geo access within a CDN endpoint. Each geo filter defines an access rule to a specified path or content, e.g. block APAC for path /pictures/ |  [optional] |
|**isCompressionEnabled** | **Boolean** | Indicates whether content compression is enabled on CDN. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won&#39;t be compressed on CDN when requested content is smaller than 1 byte or larger than 1 MB. |  [optional] |
|**isHttpAllowed** | **Boolean** | Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**isHttpsAllowed** | **Boolean** | Indicates whether HTTPS traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**optimizationType** | **OptimizationType** |  |  [optional] |
|**originHostHeader** | **String** | The host header value sent to the origin with each request. This property at Endpoint is only allowed when endpoint uses single origin and can be overridden by the same property specified at origin.If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. |  [optional] |
|**originPath** | **String** | A directory path on the origin that CDN can use to retrieve content from, e.g. contoso.cloudapp.net/originpath. |  [optional] |
|**probePath** | **String** | Path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the origin path. This property is only relevant when using a single origin. |  [optional] |
|**queryStringCachingBehavior** | **QueryStringCachingBehavior** |  |  [optional] |



