

# VmwareDiskConfig

VMware disk config details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backingType** | [**BackingTypeEnum**](#BackingTypeEnum) | VMDK backing type. |  [optional] |
|**rdmCompatibility** | [**RdmCompatibilityEnum**](#RdmCompatibilityEnum) | RDM compatibility mode. |  [optional] |
|**shared** | **Boolean** | Is VMDK shared with other VMs. |  [optional] |
|**vmdkMode** | [**VmdkModeEnum**](#VmdkModeEnum) | VMDK disk mode. |  [optional] |



## Enum: BackingTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BACKING_TYPE_UNSPECIFIED&quot; |
| FLAT_V1 | &quot;BACKING_TYPE_FLAT_V1&quot; |
| FLAT_V2 | &quot;BACKING_TYPE_FLAT_V2&quot; |
| PMEM | &quot;BACKING_TYPE_PMEM&quot; |
| RDM_V1 | &quot;BACKING_TYPE_RDM_V1&quot; |
| RDM_V2 | &quot;BACKING_TYPE_RDM_V2&quot; |
| SESPARSE | &quot;BACKING_TYPE_SESPARSE&quot; |
| SESPARSE_V1 | &quot;BACKING_TYPE_SESPARSE_V1&quot; |
| SESPARSE_V2 | &quot;BACKING_TYPE_SESPARSE_V2&quot; |



## Enum: RdmCompatibilityEnum

| Name | Value |
|---- | -----|
| RDM_COMPATIBILITY_UNSPECIFIED | &quot;RDM_COMPATIBILITY_UNSPECIFIED&quot; |
| PHYSICAL_COMPATIBILITY | &quot;PHYSICAL_COMPATIBILITY&quot; |
| VIRTUAL_COMPATIBILITY | &quot;VIRTUAL_COMPATIBILITY&quot; |



## Enum: VmdkModeEnum

| Name | Value |
|---- | -----|
| VMDK_MODE_UNSPECIFIED | &quot;VMDK_MODE_UNSPECIFIED&quot; |
| DEPENDENT | &quot;DEPENDENT&quot; |
| INDEPENDENT_PERSISTENT | &quot;INDEPENDENT_PERSISTENT&quot; |
| INDEPENDENT_NONPERSISTENT | &quot;INDEPENDENT_NONPERSISTENT&quot; |



