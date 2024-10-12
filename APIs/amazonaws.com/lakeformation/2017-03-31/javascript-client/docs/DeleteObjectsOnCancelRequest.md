# AwsLakeFormation.DeleteObjectsOnCancelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The Glue data catalog that contains the governed table. Defaults to the current account ID. | [optional] 
**databaseName** | **String** | The database that contains the governed table. | 
**tableName** | **String** | The name of the governed table. | 
**transactionId** | **String** | ID of the transaction that the writes occur in. | 
**objects** | [**[VirtualObject]**](VirtualObject.md) | A list of VirtualObject structures, which indicates the Amazon S3 objects to be deleted if the transaction cancels. | 


