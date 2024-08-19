

# DiskMigrationJobsCreateRequestInnerProperties

Managed disk properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualSizeGB** | **Long** | The actual size of disk in GB. |  [optional] [readonly] |
|**diskId** | **String** | The disk id. |  [optional] |
|**diskSku** | [**DiskSkuEnum**](#DiskSkuEnum) | Disk Sku. |  [optional] |
|**diskType** | [**DiskTypeEnum**](#DiskTypeEnum) | Disk resource type. |  [optional] |
|**managedBy** | **String** | Compute resource Uri which owns this disk. |  [optional] [readonly] |
|**provisionSizeGB** | **Long** | The provision size of disk in GB. |  [optional] [readonly] |
|**sharePath** | **String** | The disk share path. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Disk State. |  [optional] |
|**userResourceId** | **String** | The disk resource Uri from user view. |  [optional] [readonly] |



## Enum: DiskSkuEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| STANDARD_ZRS | &quot;Standard_ZRS&quot; |
| STANDARD_GRS | &quot;Standard_GRS&quot; |
| STANDARD_RAGRS | &quot;Standard_RAGRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |
| STANDARD_SSD_LRS | &quot;StandardSSD_LRS&quot; |
| ULTRA_SSD_LRS | &quot;UltraSSD_LRS&quot; |



## Enum: DiskTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| DISK | &quot;Disk&quot; |
| SNAPSHOT | &quot;Snapshot&quot; |
| RESTORE_POINT | &quot;RestorePoint&quot; |
| MANAGED_BLOB | &quot;ManagedBlob&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| UNATTACHED | &quot;Unattached&quot; |
| ATTACHED | &quot;Attached&quot; |
| RESERVED | &quot;Reserved&quot; |
| ACTIVE_SAS | &quot;ActiveSAS&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| ALL | &quot;All&quot; |
| RECOMMENDED | &quot;Recommended&quot; |
| OFFLINE_MIGRATION | &quot;OfflineMigration&quot; |
| ONLINE_MIGRATION | &quot;OnlineMigration&quot; |



