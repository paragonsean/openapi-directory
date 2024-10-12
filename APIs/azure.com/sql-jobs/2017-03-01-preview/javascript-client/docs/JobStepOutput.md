# SqlManagementClient.JobStepOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **String** | The resource ID of the credential to use to connect to the output destination. | 
**databaseName** | **String** | The output destination database. | 
**resourceGroupName** | **String** | The output destination resource group. | [optional] 
**schemaName** | **String** | The output destination schema. | [optional] [default to &#39;dbo&#39;]
**serverName** | **String** | The output destination server name. | 
**subscriptionId** | **String** | The output destination subscription id. | [optional] 
**tableName** | **String** | The output destination table. | 
**type** | **String** | The output destination type. | [optional] [default to &#39;SqlDatabase&#39;]



## Enum: TypeEnum


* `SqlDatabase` (value: `"SqlDatabase"`)




