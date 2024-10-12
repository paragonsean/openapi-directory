

# EndpointProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentTypesToCompress** | **List&lt;String&gt;** | List of content types on which compression will be applied. The value for the elements should be a valid MIME type. |  [optional] |
|**hostName** | **String** | The host name of the endpoint {endpointName}.{DNSZone} |  [optional] [readonly] |
|**isCompressionEnabled** | **Boolean** | Indicates whether the compression is enabled. Default value is false. If compression is enabled, the content transferred from cdn endpoint to end user will be compressed. The requested content must be larger than 1 byte and smaller than 1 MB. |  [optional] |
|**isHttpAllowed** | **Boolean** | Indicates whether HTTP traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**isHttpsAllowed** | **Boolean** | Indicates whether https traffic is allowed on the endpoint. Default value is true. At least one protocol (HTTP or HTTPS) must be allowed. |  [optional] |
|**originHostHeader** | **String** | The host header the CDN provider will send along with content requests to origins. The default value is the host name of the origin. |  [optional] |
|**originPath** | **String** | The path used for origin requests. |  [optional] |
|**origins** | [**List&lt;DeepCreatedOrigin&gt;**](DeepCreatedOrigin.md) | The set of origins for the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**queryStringCachingBehavior** | **QueryStringCachingBehavior** |  |  [optional] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | Resource status of the endpoint. |  [optional] [readonly] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| RUNNING | &quot;Running&quot; |
| STARTING | &quot;Starting&quot; |
| STOPPED | &quot;Stopped&quot; |
| STOPPING | &quot;Stopping&quot; |



