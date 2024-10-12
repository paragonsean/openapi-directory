# DataBoxEdgeManagementClient.StorageAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blobEndpoint** | **String** | BlobEndpoint of Storage Account | [optional] [readonly] 
**containerCount** | **Number** | The Container Count. Present only for Storage Accounts with DataPolicy set to Cloud. | [optional] [readonly] 
**dataPolicy** | **String** | Data policy of the storage Account. | [optional] 
**description** | **String** | Description for the storage Account. | [optional] 
**storageAccountCredentialId** | **String** | Storage Account Credential Id | [optional] 
**storageAccountStatus** | **String** | Current status of the storage account | [optional] 



## Enum: DataPolicyEnum


* `Cloud` (value: `"Cloud"`)

* `Local` (value: `"Local"`)





## Enum: StorageAccountStatusEnum


* `OK` (value: `"OK"`)

* `Offline` (value: `"Offline"`)

* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `NeedsAttention` (value: `"NeedsAttention"`)




