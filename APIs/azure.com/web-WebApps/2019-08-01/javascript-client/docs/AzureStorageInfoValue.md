# WebAppsApiClient.AzureStorageInfoValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKey** | **String** | Access key for the storage account. | [optional] 
**accountName** | **String** | Name of the storage account. | [optional] 
**mountPath** | **String** | Path to mount the storage within the site&#39;s runtime environment. | [optional] 
**shareName** | **String** | Name of the file share (container name, for Blob storage). | [optional] 
**state** | **String** | State of the storage account. | [optional] [readonly] 
**type** | **String** | Type of storage. | [optional] 



## Enum: StateEnum


* `Ok` (value: `"Ok"`)

* `InvalidCredentials` (value: `"InvalidCredentials"`)

* `InvalidShare` (value: `"InvalidShare"`)





## Enum: TypeEnum


* `AzureFiles` (value: `"AzureFiles"`)

* `AzureBlob` (value: `"AzureBlob"`)




