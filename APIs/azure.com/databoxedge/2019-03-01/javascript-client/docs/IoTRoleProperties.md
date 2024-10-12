# DataBoxEdgeManagementClient.IoTRoleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostPlatform** | **String** | Host OS supported by the IoT role. | 
**ioTDeviceDetails** | [**IoTDeviceInfo**](IoTDeviceInfo.md) |  | 
**ioTEdgeDeviceDetails** | [**IoTDeviceInfo**](IoTDeviceInfo.md) |  | 
**roleStatus** | **String** | Role status. | 
**shareMappings** | [**[MountPointMap]**](MountPointMap.md) | Mount points of shares in role(s). | [optional] 



## Enum: HostPlatformEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: RoleStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




