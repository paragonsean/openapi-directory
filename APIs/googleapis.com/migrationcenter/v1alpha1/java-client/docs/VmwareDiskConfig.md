

# VmwareDiskConfig

VMware disk config details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backingType** | [**BackingTypeEnum**](#BackingTypeEnum) | VMDK backing type. |  [optional] |
|**rdmCompatibilityMode** | **String** | RDM compatibility mode. |  [optional] |
|**shared** | **Boolean** | Is VMDK shared with other VMs. |  [optional] |
|**vmdkDiskMode** | **String** | VMDK disk mode. |  [optional] |



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



