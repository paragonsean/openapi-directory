

# CreateOriginEndpointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorization** | [**CreateOriginEndpointRequestAuthorization**](CreateOriginEndpointRequestAuthorization.md) |  |  [optional] |
|**channelId** | **String** | The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.  |  |
|**cmafPackage** | [**CreateOriginEndpointRequestCmafPackage**](CreateOriginEndpointRequestCmafPackage.md) |  |  [optional] |
|**dashPackage** | [**CreateOriginEndpointRequestDashPackage**](CreateOriginEndpointRequestDashPackage.md) |  |  [optional] |
|**description** | **String** | A short text description of the OriginEndpoint. |  [optional] |
|**hlsPackage** | [**CreateOriginEndpointRequestHlsPackage**](CreateOriginEndpointRequestHlsPackage.md) |  |  [optional] |
|**id** | **String** | The ID of the OriginEndpoint.  The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.  |  |
|**manifestName** | **String** | A short string that will be used as the filename of the OriginEndpoint URL (defaults to \&quot;index\&quot;). |  [optional] |
|**mssPackage** | [**CreateOriginEndpointRequestMssPackage**](CreateOriginEndpointRequestMssPackage.md) |  |  [optional] |
|**origination** | [**OriginationEnum**](#OriginationEnum) | Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination  |  [optional] |
|**startoverWindowSeconds** | **Integer** | Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A collection of tags associated with a resource |  [optional] |
|**timeDelaySeconds** | **Integer** | Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.  |  [optional] |
|**whitelist** | **List&lt;String&gt;** | A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint. |  [optional] |



## Enum: OriginationEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



