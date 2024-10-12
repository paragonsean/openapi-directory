# AwsDeviceFarm.GetRunResultRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**type** | [**TestType**](TestType.md) |  | [optional] 
**platform** | [**DevicePlatform**](DevicePlatform.md) |  | [optional] 
**created** | **Date** |  | [optional] 
**status** | [**ExecutionStatus**](ExecutionStatus.md) |  | [optional] 
**result** | [**ExecutionResult**](ExecutionResult.md) |  | [optional] 
**started** | **Date** |  | [optional] 
**stopped** | **Date** |  | [optional] 
**counters** | [**RunCounters**](RunCounters.md) |  | [optional] 
**message** | **String** |  | [optional] 
**totalJobs** | **Number** |  | [optional] 
**completedJobs** | **Number** |  | [optional] 
**billingMethod** | [**BillingMethod**](BillingMethod.md) |  | [optional] 
**deviceMinutes** | [**RunDeviceMinutes**](RunDeviceMinutes.md) |  | [optional] 
**networkProfile** | [**RunNetworkProfile**](RunNetworkProfile.md) |  | [optional] 
**parsingResultUrl** | **String** |  | [optional] 
**resultCode** | [**ExecutionResultCode**](ExecutionResultCode.md) |  | [optional] 
**seed** | **Number** |  | [optional] 
**appUpload** | **String** |  | [optional] 
**eventCount** | **Number** |  | [optional] 
**jobTimeoutMinutes** | **Number** |  | [optional] 
**devicePoolArn** | **String** |  | [optional] 
**locale** | **String** |  | [optional] 
**radios** | [**ScheduleRunConfigurationRadios**](ScheduleRunConfigurationRadios.md) |  | [optional] 
**location** | [**ScheduleRunConfigurationLocation**](ScheduleRunConfigurationLocation.md) |  | [optional] 
**customerArtifactPaths** | [**RunCustomerArtifactPaths**](RunCustomerArtifactPaths.md) |  | [optional] 
**webUrl** | **String** |  | [optional] 
**skipAppResign** | **Boolean** |  | [optional] 
**testSpecArn** | **String** |  | [optional] 
**deviceSelectionResult** | [**RunDeviceSelectionResult**](RunDeviceSelectionResult.md) |  | [optional] 
**vpcConfig** | [**CreateProjectRequestVpcConfig**](CreateProjectRequestVpcConfig.md) |  | [optional] 


