# AwsElementalMediaPackage.UpdateOriginEndpointRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**CreateOriginEndpointRequestAuthorization**](CreateOriginEndpointRequestAuthorization.md) |  | [optional] 
**cmafPackage** | [**CreateOriginEndpointRequestCmafPackage**](CreateOriginEndpointRequestCmafPackage.md) |  | [optional] 
**dashPackage** | [**CreateOriginEndpointRequestDashPackage**](CreateOriginEndpointRequestDashPackage.md) |  | [optional] 
**description** | **String** | A short text description of the OriginEndpoint. | [optional] 
**hlsPackage** | [**CreateOriginEndpointRequestHlsPackage**](CreateOriginEndpointRequestHlsPackage.md) |  | [optional] 
**manifestName** | **String** | A short string that will be appended to the end of the Endpoint URL. | [optional] 
**mssPackage** | [**CreateOriginEndpointRequestMssPackage**](CreateOriginEndpointRequestMssPackage.md) |  | [optional] 
**origination** | **String** | Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination  | [optional] 
**startoverWindowSeconds** | **Number** | Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.  | [optional] 
**timeDelaySeconds** | **Number** | Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.  | [optional] 
**whitelist** | **[String]** | A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint. | [optional] 



## Enum: OriginationEnum


* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)




