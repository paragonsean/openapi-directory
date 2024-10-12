

# ServerProperties

The properties of a server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administratorLogin** | **String** | The administrator&#39;s login name of a server. Can only be specified when the server is being created (and is required for creation). |  [optional] |
|**fullyQualifiedDomainName** | **String** | The fully qualified domain name of a server. |  [optional] |
|**sslEnforcement** | **SslEnforcement** |  |  [optional] |
|**storageMB** | **Long** | The maximum storage allowed for a server. |  [optional] |
|**userVisibleState** | [**UserVisibleStateEnum**](#UserVisibleStateEnum) | A state of a server that is visible to user. |  [optional] |
|**version** | **ServerVersion** |  |  [optional] |



## Enum: UserVisibleStateEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| DROPPING | &quot;Dropping&quot; |
| DISABLED | &quot;Disabled&quot; |



