

# EndpointPropertiesUpdateParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentTypesToCompress** | **List&lt;String&gt;** | List of content types on which compression will be applied. The value for the elements should be a valid MIME type. |  [optional] |
|**isCompressionEnabled** | **Boolean** | Indicates whether content compression is enabled. Default value is false. If compression is enabled, the content transferred from the CDN endpoint to the end user will be compressed. The requested content must be larger than 1 byte and smaller than 1 MB. |  [optional] |
|**isHttpAllowed** | **Boolean** | Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**isHttpsAllowed** | **Boolean** | Indicates whether HTTPS traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**originHostHeader** | **String** | The host header the CDN provider will send along with content requests to origins. The default value is the host name of the origin. |  [optional] |
|**originPath** | **String** | The path used for origin requests. |  [optional] |
|**queryStringCachingBehavior** | **QueryStringCachingBehavior** |  |  [optional] |



