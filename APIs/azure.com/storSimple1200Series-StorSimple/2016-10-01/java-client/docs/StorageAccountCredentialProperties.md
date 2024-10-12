

# StorageAccountCredentialProperties

Storage account properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**cloudType** | [**CloudTypeEnum**](#CloudTypeEnum) | The cloud service provider |  |
|**enableSSL** | [**EnableSSLEnum**](#EnableSSLEnum) | SSL needs to be enabled or not |  |
|**endPoint** | **String** | The storage endpoint |  |
|**location** | **String** | The storage account&#39;s geo location |  [optional] |
|**login** | **String** | The storage account login |  |



## Enum: CloudTypeEnum

| Name | Value |
|---- | -----|
| AZURE | &quot;Azure&quot; |
| S3 | &quot;S3&quot; |
| S3_RRS | &quot;S3_RRS&quot; |
| OPEN_STACK | &quot;OpenStack&quot; |
| HP | &quot;HP&quot; |



## Enum: EnableSSLEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



