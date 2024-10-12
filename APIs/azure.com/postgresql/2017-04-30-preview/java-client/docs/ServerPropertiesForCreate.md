

# ServerPropertiesForCreate

The properties used to create a new server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | The mode to create a new server. |  |
|**sslEnforcement** | **SslEnforcement** |  |  [optional] |
|**storageMB** | **Long** | The maximum storage allowed for a server. |  [optional] |
|**version** | **ServerVersion** |  |  [optional] |



## Enum: CreateModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| POINT_IN_TIME_RESTORE | &quot;PointInTimeRestore&quot; |



