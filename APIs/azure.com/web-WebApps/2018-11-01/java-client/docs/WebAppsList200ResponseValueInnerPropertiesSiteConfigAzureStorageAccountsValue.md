

# WebAppsList200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue

Azure Files or Blob Storage access information value for dictionary storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKey** | **String** | Access key for the storage account. |  [optional] |
|**accountName** | **String** | Name of the storage account. |  [optional] |
|**mountPath** | **String** | Path to mount the storage within the site&#39;s runtime environment. |  [optional] |
|**shareName** | **String** | Name of the file share (container name, for Blob storage). |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the storage account. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of storage. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OK | &quot;Ok&quot; |
| INVALID_CREDENTIALS | &quot;InvalidCredentials&quot; |
| INVALID_SHARE | &quot;InvalidShare&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AZURE_FILES | &quot;AzureFiles&quot; |
| AZURE_BLOB | &quot;AzureBlob&quot; |



