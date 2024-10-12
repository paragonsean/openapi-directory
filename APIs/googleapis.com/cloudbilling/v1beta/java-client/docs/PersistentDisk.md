

# PersistentDisk

Specification of a persistent disk attached to a VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskSize** | [**Usage**](Usage.md) |  |  [optional] |
|**diskType** | **String** | The [disk type](https://cloud.google.com/compute/docs/disks#disk-types). For example: \&quot;pd-standard\&quot;. |  [optional] |
|**provisionedIops** | [**Usage**](Usage.md) |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The geographic scope of the disk. Defaults to &#x60;SCOPE_ZONAL&#x60; if not specified. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SCOPE_UNSPECIFIED&quot; |
| ZONAL | &quot;SCOPE_ZONAL&quot; |
| REGIONAL | &quot;SCOPE_REGIONAL&quot; |



