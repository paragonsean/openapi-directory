

# NewDeviceEvent

An event generated when a new device is ready to be managed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceId** | **String** | The Android ID of the device. This field will always be present. |  [optional] |
|**dpcPackageName** | **String** | Policy app on the device. |  [optional] |
|**managementType** | [**ManagementTypeEnum**](#ManagementTypeEnum) | Identifies the extent to which the device is controlled by an Android EMM in various deployment configurations. Possible values include: - \&quot;managedDevice\&quot;, a device where the DPC is set as device owner, - \&quot;managedProfile\&quot;, a device where the DPC is set as profile owner.  |  [optional] |
|**userId** | **String** | The ID of the user. This field will always be present. |  [optional] |



## Enum: ManagementTypeEnum

| Name | Value |
|---- | -----|
| MANAGED_DEVICE | &quot;managedDevice&quot; |
| MANAGED_PROFILE | &quot;managedProfile&quot; |



