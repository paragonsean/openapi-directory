# SqlManagementClient.ManagedInstanceKeyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The key creation date. | [optional] [readonly] 
**serverKeyType** | **String** | The key type like &#39;ServiceManaged&#39;, &#39;AzureKeyVault&#39;. | 
**thumbprint** | **String** | Thumbprint of the key. | [optional] [readonly] 
**uri** | **String** | The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required. | [optional] 



## Enum: ServerKeyTypeEnum


* `ServiceManaged` (value: `"ServiceManaged"`)

* `AzureKeyVault` (value: `"AzureKeyVault"`)




