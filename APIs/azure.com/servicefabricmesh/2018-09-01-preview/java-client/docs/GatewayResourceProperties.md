

# GatewayResourceProperties

This type describes properties of a gateway resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |
|**description** | **String** | User readable description of the gateway. |  [optional] |
|**destinationNetwork** | [**NetworkRef**](NetworkRef.md) |  |  |
|**http** | [**List&lt;HttpConfig&gt;**](HttpConfig.md) | Configuration for http connectivity for this gateway. |  [optional] |
|**ipAddress** | **String** | IP address of the gateway. This is populated in the response and is ignored for incoming requests. |  [optional] [readonly] |
|**sourceNetwork** | [**NetworkRef**](NetworkRef.md) |  |  |
|**status** | **ResourceStatus** |  |  [optional] |
|**statusDetails** | **String** | Gives additional information about the current status of the gateway. |  [optional] [readonly] |
|**tcp** | [**List&lt;TcpConfig&gt;**](TcpConfig.md) | Configuration for tcp connectivity for this gateway. |  [optional] |



