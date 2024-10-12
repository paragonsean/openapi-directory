

# DeviceProperties

The properties of the StorSimple device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationTime** | **OffsetDateTime** | The UTC time at which the device was activated |  |
|**activeController** | [**ActiveControllerEnum**](#ActiveControllerEnum) | The identifier of the active controller of the device. |  |
|**agentGroupVersion** | **Integer** | The device agent group version. |  [optional] |
|**availableLocalStorageInBytes** | **Long** | The storage in bytes that is available locally on the device. |  [optional] |
|**availableTieredStorageInBytes** | **Long** | The storage in bytes that is available on the device for tiered volumes. |  [optional] |
|**culture** | **String** | The language culture setting on the device. For eg: \&quot;en-US\&quot; |  |
|**details** | [**DeviceDetails**](DeviceDetails.md) |  |  [optional] |
|**deviceConfigurationStatus** | [**DeviceConfigurationStatusEnum**](#DeviceConfigurationStatusEnum) | The current configuration status of the device. |  |
|**deviceDescription** | **String** | The device description. |  |
|**deviceLocation** | **String** | The location of the virtual appliance. |  [optional] |
|**deviceSoftwareVersion** | **String** | The version number of the software running on the device. |  |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | The type of the device. |  |
|**friendlyName** | **String** | The friendly name of the device. |  |
|**friendlySoftwareName** | **String** | The friendly name of the software running on the device. |  [optional] |
|**friendlySoftwareVersion** | **String** | The device friendly software version. |  |
|**modelDescription** | **String** | The device model. |  |
|**networkInterfaceCardCount** | **Integer** | The number of network interface cards |  [optional] |
|**provisionedLocalStorageInBytes** | **Long** | The storage in bytes used for locally pinned volumes on the device (including additional local reservation). |  [optional] |
|**provisionedTieredStorageInBytes** | **Long** | The storage in bytes that has been provisioned on the device for tiered volumes. |  [optional] |
|**provisionedVolumeSizeInBytes** | **Long** | Total capacity in bytes of tiered and locally pinned volumes on the device |  [optional] |
|**rolloverDetails** | [**DeviceRolloverDetails**](DeviceRolloverDetails.md) |  |  [optional] |
|**serialNumber** | **String** | The serial number. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the device. |  |
|**targetIqn** | **String** | The target IQN. |  |
|**totalTieredStorageInBytes** | **Long** | The total tiered storage available on the device in bytes. |  [optional] |
|**usingStorageInBytes** | **Long** | The storage in bytes that is currently being used on the device, including both local and cloud. |  [optional] |
|**virtualMachineApiType** | [**VirtualMachineApiTypeEnum**](#VirtualMachineApiTypeEnum) | The virtual machine API type. |  [optional] [readonly] |



## Enum: ActiveControllerEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NONE | &quot;None&quot; |
| CONTROLLER0 | &quot;Controller0&quot; |
| CONTROLLER1 | &quot;Controller1&quot; |



## Enum: DeviceConfigurationStatusEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;Complete&quot; |
| PENDING | &quot;Pending&quot; |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SERIES8000_VIRTUAL_APPLIANCE | &quot;Series8000VirtualAppliance&quot; |
| SERIES8000_PHYSICAL_APPLIANCE | &quot;Series8000PhysicalAppliance&quot; |



## Enum: StatusEnum

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



## Enum: VirtualMachineApiTypeEnum

| Name | Value |
|---- | -----|
| CLASSIC | &quot;Classic&quot; |
| ARM | &quot;Arm&quot; |



