# SeaBreezeManagementClient.GatewayProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | User readable description of the gateway. | [optional] 
**destinationNetwork** | [**NetworkRef**](NetworkRef.md) |  | 
**http** | [**[HttpConfig]**](HttpConfig.md) | Configuration for http connectivity for this gateway. | [optional] 
**ipAddress** | **String** | IP address of the gateway. This is populated in the response and is ignored for incoming requests. | [optional] [readonly] 
**sourceNetwork** | [**NetworkRef**](NetworkRef.md) |  | 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**statusDetails** | **String** | Gives additional information about the current status of the gateway. | [optional] [readonly] 
**tcp** | [**[TcpConfig]**](TcpConfig.md) | Configuration for tcp connectivity for this gateway. | [optional] 


