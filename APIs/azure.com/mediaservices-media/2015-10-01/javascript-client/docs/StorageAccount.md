# MediaServicesManagementClient.StorageAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The id of the storage account resource. Media Services relies on tables and queues as well as blobs, so the primary storage account must be a Standard Storage account (either Microsoft.ClassicStorage or Microsoft.Storage). Blob only storage accounts can be added as secondary storage accounts (isPrimary false). | 
**isPrimary** | **Boolean** | Is this storage account resource the primary storage account for the Media Service resource. Blob only storage must set this to false. | 


