

# JobStepOutput

The output configuration of a job step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credential** | **String** | The resource ID of the credential to use to connect to the output destination. |  |
|**databaseName** | **String** | The output destination database. |  |
|**resourceGroupName** | **String** | The output destination resource group. |  [optional] |
|**schemaName** | **String** | The output destination schema. |  [optional] |
|**serverName** | **String** | The output destination server name. |  |
|**subscriptionId** | **UUID** | The output destination subscription id. |  [optional] |
|**tableName** | **String** | The output destination table. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The output destination type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SQL_DATABASE | &quot;SqlDatabase&quot; |



