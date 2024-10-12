

# AzureContainerInfo

Azure container mapping of the endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerName** | **String** | Container name (Based on the data format specified, this represents the name of Azure Files/Page blob/Block blob). |  |
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Storage format used for the file represented by the share. |  |
|**storageAccountCredentialId** | **String** | ID of the storage account credential used to access storage. |  |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| BLOCK_BLOB | &quot;BlockBlob&quot; |
| PAGE_BLOB | &quot;PageBlob&quot; |
| AZURE_FILE | &quot;AzureFile&quot; |



