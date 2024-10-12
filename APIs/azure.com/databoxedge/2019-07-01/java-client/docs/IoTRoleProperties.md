

# IoTRoleProperties

IoT role properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostPlatform** | [**HostPlatformEnum**](#HostPlatformEnum) | Host OS supported by the IoT role. |  |
|**ioTDeviceDetails** | [**IoTDeviceInfo**](IoTDeviceInfo.md) |  |  |
|**ioTEdgeDeviceDetails** | [**IoTDeviceInfo**](IoTDeviceInfo.md) |  |  |
|**roleStatus** | [**RoleStatusEnum**](#RoleStatusEnum) | Role status. |  |
|**shareMappings** | [**List&lt;MountPointMap&gt;**](MountPointMap.md) | Mount points of shares in role(s). |  [optional] |



## Enum: HostPlatformEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: RoleStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



