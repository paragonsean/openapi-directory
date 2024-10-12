

# BackupVaultConfigProperties

Backup vault config details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enhancedSecurityState** | [**EnhancedSecurityStateEnum**](#EnhancedSecurityStateEnum) | Enabled or Disabled. |  [optional] |
|**storageType** | [**StorageTypeEnum**](#StorageTypeEnum) | Storage type. |  [optional] |
|**storageTypeState** | [**StorageTypeStateEnum**](#StorageTypeStateEnum) | Locked or Unlocked. Once a machine is registered against a resource, the storageTypeState is always Locked. |  [optional] |



## Enum: EnhancedSecurityStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: StorageTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| GEO_REDUNDANT | &quot;GeoRedundant&quot; |
| LOCALLY_REDUNDANT | &quot;LocallyRedundant&quot; |



## Enum: StorageTypeStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| LOCKED | &quot;Locked&quot; |
| UNLOCKED | &quot;Unlocked&quot; |



