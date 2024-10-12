

# StorageAccountCredentialProperties

The storage account credential properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**endPoint** | **String** | The storage endpoint |  |
|**sslStatus** | [**SslStatusEnum**](#SslStatusEnum) | Signifies whether SSL needs to be enabled or not. |  |
|**volumesCount** | **Integer** | The count of volumes using this storage account credential. |  [optional] [readonly] |



## Enum: SslStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



