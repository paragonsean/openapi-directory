

# VmmVirtualMachineDetails

VMM fabric provider specific VM settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskDetails** | [**List&lt;DiskDetails&gt;**](DiskDetails.md) | The Last successful failover time. |  [optional] |
|**generation** | **String** | The id of the object in fabric. |  [optional] |
|**hasFibreChannelAdapter** | [**HasFibreChannelAdapterEnum**](#HasFibreChannelAdapterEnum) | A value indicating whether the VM has a fibre channel adapter attached. String value of {SrsDataContract.PresenceStatus} enum. |  [optional] |
|**hasPhysicalDisk** | [**HasPhysicalDiskEnum**](#HasPhysicalDiskEnum) | A value indicating whether the VM has a physical disk attached. String value of {SrsDataContract.PresenceStatus} enum. |  [optional] |
|**hasSharedVhd** | [**HasSharedVhdEnum**](#HasSharedVhdEnum) | A value indicating whether the VM has a shared VHD attached. String value of {SrsDataContract.PresenceStatus} enum. |  [optional] |
|**osDetails** | [**OSDetails**](OSDetails.md) |  |  [optional] |
|**sourceItemId** | **String** | The source id of the object. |  [optional] |



## Enum: HasFibreChannelAdapterEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PRESENT | &quot;Present&quot; |
| NOT_PRESENT | &quot;NotPresent&quot; |



## Enum: HasPhysicalDiskEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PRESENT | &quot;Present&quot; |
| NOT_PRESENT | &quot;NotPresent&quot; |



## Enum: HasSharedVhdEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PRESENT | &quot;Present&quot; |
| NOT_PRESENT | &quot;NotPresent&quot; |



