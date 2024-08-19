# AmazonAppStream.CreateFleetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**imageName** | **String** |  | [optional] 
**imageArn** | **String** |  | [optional] 
**instanceType** | **String** |  | 
**fleetType** | [**FleetType**](FleetType.md) |  | [optional] 
**computeCapacity** | [**CreateFleetRequestComputeCapacity**](CreateFleetRequestComputeCapacity.md) |  | [optional] 
**vpcConfig** | [**CreateFleetRequestVpcConfig**](CreateFleetRequestVpcConfig.md) |  | [optional] 
**maxUserDurationInSeconds** | **Number** |  | [optional] 
**disconnectTimeoutInSeconds** | **Number** |  | [optional] 
**description** | **String** |  | [optional] 
**displayName** | **String** |  | [optional] 
**enableDefaultInternetAccess** | **Boolean** |  | [optional] 
**domainJoinInfo** | [**CreateFleetRequestDomainJoinInfo**](CreateFleetRequestDomainJoinInfo.md) |  | [optional] 
**tags** | **Object** |  | [optional] 
**idleDisconnectTimeoutInSeconds** | **Number** |  | [optional] 
**iamRoleArn** | **String** |  | [optional] 
**streamView** | [**StreamView**](StreamView.md) |  | [optional] 
**platform** | [**PlatformType**](PlatformType.md) |  | [optional] 
**maxConcurrentSessions** | **Number** |  | [optional] 
**usbDeviceFilterStrings** | **Array** |  | [optional] 
**sessionScriptS3Location** | [**CreateFleetRequestSessionScriptS3Location**](CreateFleetRequestSessionScriptS3Location.md) |  | [optional] 


