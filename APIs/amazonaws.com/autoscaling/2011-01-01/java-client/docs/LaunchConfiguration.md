

# LaunchConfiguration

Describes a launch configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**launchConfigurationName** | [**String**](String.md) |  |  |
|**launchConfigurationARN** | [**String**](String.md) |  |  [optional] |
|**imageId** | [**String**](String.md) |  |  |
|**keyName** | [**String**](String.md) |  |  [optional] |
|**securityGroups** | [**List**](List.md) |  |  [optional] |
|**classicLinkVPCId** | [**String**](String.md) |  |  [optional] |
|**classicLinkVPCSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**userData** | [**String**](String.md) |  |  [optional] |
|**instanceType** | [**String**](String.md) |  |  |
|**kernelId** | [**String**](String.md) |  |  [optional] |
|**ramdiskId** | [**String**](String.md) |  |  [optional] |
|**blockDeviceMappings** | [**List**](List.md) |  |  [optional] |
|**instanceMonitoring** | [**LaunchConfigurationInstanceMonitoring**](LaunchConfigurationInstanceMonitoring.md) |  |  [optional] |
|**spotPrice** | [**String**](String.md) |  |  [optional] |
|**iamInstanceProfile** | [**String**](String.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**ebsOptimized** | [**Boolean**](Boolean.md) |  |  [optional] |
|**associatePublicIpAddress** | [**Boolean**](Boolean.md) |  |  [optional] |
|**placementTenancy** | [**String**](String.md) |  |  [optional] |
|**metadataOptions** | [**CreateLaunchConfigurationTypeMetadataOptions**](CreateLaunchConfigurationTypeMetadataOptions.md) |  |  [optional] |



