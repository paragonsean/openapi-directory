# PostgreSqlManagementClient.ServerPropertiesForCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createMode** | **String** | The mode to create a new server. | 
**sslEnforcement** | [**SslEnforcement**](SslEnforcement.md) |  | [optional] 
**storageProfile** | [**StorageProfile**](StorageProfile.md) |  | [optional] 
**version** | [**ServerVersion**](ServerVersion.md) |  | [optional] 



## Enum: CreateModeEnum


* `Default` (value: `"Default"`)

* `PointInTimeRestore` (value: `"PointInTimeRestore"`)

* `GeoRestore` (value: `"GeoRestore"`)

* `Replica` (value: `"Replica"`)




