# MySqlManagementClient.ServerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administratorLogin** | **String** | The administrator&#39;s login name of a server. Can only be specified when the server is being created (and is required for creation). | [optional] 
**fullyQualifiedDomainName** | **String** | The fully qualified domain name of a server. | [optional] 
**sslEnforcement** | [**SslEnforcement**](SslEnforcement.md) |  | [optional] 
**storageMB** | **Number** | The maximum storage allowed for a server. | [optional] 
**userVisibleState** | **String** | A state of a server that is visible to user. | [optional] 
**version** | [**ServerVersion**](ServerVersion.md) |  | [optional] 



## Enum: UserVisibleStateEnum


* `Ready` (value: `"Ready"`)

* `Dropping` (value: `"Dropping"`)

* `Disabled` (value: `"Disabled"`)




