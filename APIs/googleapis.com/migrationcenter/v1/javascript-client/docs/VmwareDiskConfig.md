# MigrationCenterApi.VmwareDiskConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backingType** | **String** | VMDK backing type. | [optional] 
**rdmCompatibility** | **String** | RDM compatibility mode. | [optional] 
**shared** | **Boolean** | Is VMDK shared with other VMs. | [optional] 
**vmdkMode** | **String** | VMDK disk mode. | [optional] 



## Enum: BackingTypeEnum


* `UNSPECIFIED` (value: `"BACKING_TYPE_UNSPECIFIED"`)

* `FLAT_V1` (value: `"BACKING_TYPE_FLAT_V1"`)

* `FLAT_V2` (value: `"BACKING_TYPE_FLAT_V2"`)

* `PMEM` (value: `"BACKING_TYPE_PMEM"`)

* `RDM_V1` (value: `"BACKING_TYPE_RDM_V1"`)

* `RDM_V2` (value: `"BACKING_TYPE_RDM_V2"`)

* `SESPARSE` (value: `"BACKING_TYPE_SESPARSE"`)

* `SESPARSE_V1` (value: `"BACKING_TYPE_SESPARSE_V1"`)

* `SESPARSE_V2` (value: `"BACKING_TYPE_SESPARSE_V2"`)





## Enum: RdmCompatibilityEnum


* `RDM_COMPATIBILITY_UNSPECIFIED` (value: `"RDM_COMPATIBILITY_UNSPECIFIED"`)

* `PHYSICAL_COMPATIBILITY` (value: `"PHYSICAL_COMPATIBILITY"`)

* `VIRTUAL_COMPATIBILITY` (value: `"VIRTUAL_COMPATIBILITY"`)





## Enum: VmdkModeEnum


* `VMDK_MODE_UNSPECIFIED` (value: `"VMDK_MODE_UNSPECIFIED"`)

* `DEPENDENT` (value: `"DEPENDENT"`)

* `INDEPENDENT_PERSISTENT` (value: `"INDEPENDENT_PERSISTENT"`)

* `INDEPENDENT_NONPERSISTENT` (value: `"INDEPENDENT_NONPERSISTENT"`)




