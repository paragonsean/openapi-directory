# MySqlManagementClient.ServerPropertiesForCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createMode** | **String** | The mode to create a new server. | 
**sslEnforcement** | [**SslEnforcement**](SslEnforcement.md) |  | [optional] 
**storageMB** | **Number** | The maximum storage allowed for a server. | [optional] 
**version** | [**ServerVersion**](ServerVersion.md) |  | [optional] 



## Enum: CreateModeEnum


* `Default` (value: `"Default"`)

* `PointInTimeRestore` (value: `"PointInTimeRestore"`)




