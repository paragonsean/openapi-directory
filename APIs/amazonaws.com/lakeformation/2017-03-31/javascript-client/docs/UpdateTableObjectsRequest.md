# AwsLakeFormation.UpdateTableObjectsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The catalog containing the governed table to update. Defaults to the caller’s account ID. | [optional] 
**databaseName** | **String** | The database containing the governed table to update. | 
**tableName** | **String** | The governed table to update. | 
**transactionId** | **String** | The transaction at which to do the write. | [optional] 
**writeOperations** | [**[WriteOperation]**](WriteOperation.md) | A list of &lt;code&gt;WriteOperation&lt;/code&gt; objects that define an object to add to or delete from the manifest for a governed table. | 


