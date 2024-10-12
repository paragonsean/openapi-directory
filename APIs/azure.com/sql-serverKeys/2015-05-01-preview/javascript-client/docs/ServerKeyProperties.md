# SqlManagementClient.ServerKeyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The server key creation date. | [optional] 
**serverKeyType** | **String** | The server key type like &#39;ServiceManaged&#39;, &#39;AzureKeyVault&#39;. | 
**subregion** | **String** | Subregion of the server key. | [optional] [readonly] 
**thumbprint** | **String** | Thumbprint of the server key. | [optional] 
**uri** | **String** | The URI of the server key. | [optional] 



## Enum: ServerKeyTypeEnum


* `ServiceManaged` (value: `"ServiceManaged"`)

* `AzureKeyVault` (value: `"AzureKeyVault"`)




