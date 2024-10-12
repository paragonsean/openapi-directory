# ServiceBusManagementClient.DestinationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveNameFormat** | **String** | Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order | [optional] 
**blobContainer** | **String** | Blob container Name | [optional] 
**storageAccountResourceId** | **String** | Resource id of the storage account to be used to create the blobs | [optional] 


