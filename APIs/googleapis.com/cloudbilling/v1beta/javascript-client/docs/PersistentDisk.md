# CloudBillingApi.PersistentDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskSize** | [**Usage**](Usage.md) |  | [optional] 
**diskType** | **String** | The [disk type](https://cloud.google.com/compute/docs/disks#disk-types). For example: \&quot;pd-standard\&quot;. | [optional] 
**provisionedIops** | [**Usage**](Usage.md) |  | [optional] 
**scope** | **String** | The geographic scope of the disk. Defaults to &#x60;SCOPE_ZONAL&#x60; if not specified. | [optional] 



## Enum: ScopeEnum


* `UNSPECIFIED` (value: `"SCOPE_UNSPECIFIED"`)

* `ZONAL` (value: `"SCOPE_ZONAL"`)

* `REGIONAL` (value: `"SCOPE_REGIONAL"`)




