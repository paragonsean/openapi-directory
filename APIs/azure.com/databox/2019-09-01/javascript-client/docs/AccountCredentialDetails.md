# DataBoxManagementClient.AccountCredentialDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountConnectionString** | **String** | Connection string of the account endpoint to use the account as a storage endpoint on the device. | [optional] [readonly] 
**accountName** | **String** | Name of the account. | [optional] [readonly] 
**dataDestinationType** | **String** | Data Destination Type. | [optional] [readonly] 
**shareCredentialDetails** | [**[ShareCredentialDetails]**](ShareCredentialDetails.md) | Per share level unencrypted access credentials. | [optional] [readonly] 



## Enum: DataDestinationTypeEnum


* `StorageAccount` (value: `"StorageAccount"`)

* `ManagedDisk` (value: `"ManagedDisk"`)




