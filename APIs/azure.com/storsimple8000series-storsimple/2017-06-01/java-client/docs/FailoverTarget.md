

# FailoverTarget

Represents the eligibility of a device as a failover target device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableLocalStorageInBytes** | **Long** | The amount of free local storage available on the device in bytes. |  [optional] |
|**availableTieredStorageInBytes** | **Long** | The amount of free tiered storage available for the device in bytes. |  [optional] |
|**dataContainersCount** | **Integer** | The count of data containers on the device. |  [optional] |
|**deviceId** | **String** | The path ID of the device. |  [optional] |
|**deviceLocation** | **String** | The geo location (applicable only for cloud appliances) of the device. |  [optional] |
|**deviceSoftwareVersion** | **String** | The software version of the device. |  [optional] |
|**deviceStatus** | [**DeviceStatusEnum**](#DeviceStatusEnum) | The status of the device. |  [optional] |
|**eligibilityResult** | [**TargetEligibilityResult**](TargetEligibilityResult.md) |  |  [optional] |
|**friendlyDeviceSoftwareVersion** | **String** | The friendly name for the current version of software on the device. |  [optional] |
|**modelDescription** | **String** | The model number of the device. |  [optional] |
|**volumesCount** | **Integer** | The count of volumes on the device. |  [optional] |



## Enum: DeviceStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |
| DEACTIVATED | &quot;Deactivated&quot; |
| REQUIRES_ATTENTION | &quot;RequiresAttention&quot; |
| MAINTENANCE_MODE | &quot;MaintenanceMode&quot; |
| CREATING | &quot;Creating&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| DEACTIVATING | &quot;Deactivating&quot; |
| DELETED | &quot;Deleted&quot; |
| READY_TO_SETUP | &quot;ReadyToSetup&quot; |



