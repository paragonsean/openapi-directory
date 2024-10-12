# AmazonAppStream.CreateFleetResultFleet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** |  | 
**name** | **String** |  | 
**displayName** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**imageName** | **String** |  | [optional] 
**imageArn** | **String** |  | [optional] 
**instanceType** | **String** |  | 
**fleetType** | [**FleetType**](FleetType.md) |  | [optional] 
**computeCapacityStatus** | [**FleetComputeCapacityStatus**](FleetComputeCapacityStatus.md) |  | 
**maxUserDurationInSeconds** | **Number** |  | [optional] 
**disconnectTimeoutInSeconds** | **Number** |  | [optional] 
**state** | [**FleetState**](FleetState.md) |  | 
**vpcConfig** | [**FleetVpcConfig**](FleetVpcConfig.md) |  | [optional] 
**createdTime** | **Date** |  | [optional] 
**fleetErrors** | **Array** |  | [optional] 
**enableDefaultInternetAccess** | **Boolean** |  | [optional] 
**domainJoinInfo** | [**UpdateFleetRequestDomainJoinInfo**](UpdateFleetRequestDomainJoinInfo.md) |  | [optional] 
**idleDisconnectTimeoutInSeconds** | **Number** |  | [optional] 
**iamRoleArn** | **String** |  | [optional] 
**streamView** | [**StreamView**](StreamView.md) |  | [optional] 
**platform** | [**PlatformType**](PlatformType.md) |  | [optional] 
**maxConcurrentSessions** | **Number** |  | [optional] 
**usbDeviceFilterStrings** | **Array** |  | [optional] 
**sessionScriptS3Location** | [**CreateFleetRequestSessionScriptS3Location**](CreateFleetRequestSessionScriptS3Location.md) |  | [optional] 


