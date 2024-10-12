# AmazonAppStream.UpdateFleetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageName** | **String** |  | [optional] 
**imageArn** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**instanceType** | **String** |  | [optional] 
**computeCapacity** | [**UpdateFleetRequestComputeCapacity**](UpdateFleetRequestComputeCapacity.md) |  | [optional] 
**vpcConfig** | [**UpdateFleetRequestVpcConfig**](UpdateFleetRequestVpcConfig.md) |  | [optional] 
**maxUserDurationInSeconds** | **Number** |  | [optional] 
**disconnectTimeoutInSeconds** | **Number** |  | [optional] 
**deleteVpcConfig** | **Boolean** |  | [optional] 
**description** | **String** |  | [optional] 
**displayName** | **String** |  | [optional] 
**enableDefaultInternetAccess** | **Boolean** |  | [optional] 
**domainJoinInfo** | [**UpdateFleetRequestDomainJoinInfo**](UpdateFleetRequestDomainJoinInfo.md) |  | [optional] 
**idleDisconnectTimeoutInSeconds** | **Number** |  | [optional] 
**attributesToDelete** | **Array** |  | [optional] 
**iamRoleArn** | **String** |  | [optional] 
**streamView** | [**StreamView**](StreamView.md) |  | [optional] 
**platform** | [**PlatformType**](PlatformType.md) |  | [optional] 
**maxConcurrentSessions** | **Number** |  | [optional] 
**usbDeviceFilterStrings** | **Array** |  | [optional] 
**sessionScriptS3Location** | [**UpdateFleetRequestSessionScriptS3Location**](UpdateFleetRequestSessionScriptS3Location.md) |  | [optional] 


