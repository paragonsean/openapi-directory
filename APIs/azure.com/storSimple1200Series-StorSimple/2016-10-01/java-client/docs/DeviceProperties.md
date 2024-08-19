

# DeviceProperties

Encases all the properties of the Device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationTime** | **OffsetDateTime** | The UTC time at which the device was activated |  [optional] |
|**allowedDeviceOperations** | [**List&lt;AllowedDeviceOperationsEnum&gt;**](#List&lt;AllowedDeviceOperationsEnum&gt;) | Operations that are allowed on the device based on its current state |  [optional] |
|**culture** | **String** | Language culture setting on the device. For eg: \&quot;en-US\&quot; |  [optional] |
|**details** | [**DeviceDetails**](DeviceDetails.md) |  |  [optional] |
|**deviceCapabilities** | [**List&lt;DeviceCapabilitiesEnum&gt;**](#List&lt;DeviceCapabilitiesEnum&gt;) | Device can be configured either as FileServer or IscsiServer |  [optional] |
|**deviceConfigurationStatus** | [**DeviceConfigurationStatusEnum**](#DeviceConfigurationStatusEnum) | \&quot;Complete\&quot; if the device has been successfully registered as File/IscsiServer and the creation of share/volume is complete, \&quot;Pending\&quot; if the device is only registered but the creation of share/volume is complete is still pending |  [optional] |
|**deviceDescription** | **String** | Short description given for the device |  [optional] |
|**deviceSoftwareVersion** | **String** | Version number of the software running on the device |  [optional] |
|**domainName** | **String** | Fully qualified name of the domain to which the device is attached |  [optional] |
|**friendlySoftwareName** | **String** | Friendly name for the software version |  [optional] |
|**modelDescription** | **String** | Name of the device model |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the device |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the device |  [optional] |



## Enum: List&lt;AllowedDeviceOperationsEnum&gt;

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DELETE | &quot;Delete&quot; |
| DELETE_WITH_WARNING | &quot;DeleteWithWarning&quot; |
| DR_SOURCE | &quot;DRSource&quot; |
| DR_TARGET | &quot;DRTarget&quot; |
| BROWSABLE | &quot;Browsable&quot; |
| READ_ONLY_FOR_DR | &quot;ReadOnlyForDR&quot; |
| DEACTIVATE | &quot;Deactivate&quot; |



## Enum: List&lt;DeviceCapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FILE_SERVER | &quot;FileServer&quot; |
| ISCSI_SERVER | &quot;IscsiServer&quot; |



## Enum: DeviceConfigurationStatusEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;Complete&quot; |
| PENDING | &quot;Pending&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |
| REQUIRES_ATTENTION | &quot;RequiresAttention&quot; |
| MAINTENANCE_MODE | &quot;MaintenanceMode&quot; |
| CREATING | &quot;Creating&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| DELETED | &quot;Deleted&quot; |
| READY_TO_SETUP | &quot;ReadyToSetup&quot; |
| DEACTIVATED | &quot;Deactivated&quot; |
| DEACTIVATING | &quot;Deactivating&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| APPLIANCE | &quot;Appliance&quot; |
| VIRTUAL_APPLIANCE | &quot;VirtualAppliance&quot; |
| SERIES9000_ON_PREM_VIRTUAL_APPLIANCE | &quot;Series9000OnPremVirtualAppliance&quot; |
| SERIES9000_VIRTUAL_APPLIANCE | &quot;Series9000VirtualAppliance&quot; |
| SERIES9000_PHYSICAL_APPLIANCE | &quot;Series9000PhysicalAppliance&quot; |



