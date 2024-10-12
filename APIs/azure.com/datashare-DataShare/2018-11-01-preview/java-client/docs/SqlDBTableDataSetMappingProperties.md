

# SqlDBTableDataSetMappingProperties

Properties of the SQL DB table data set mapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSetId** | **String** | The id of the source data set. |  |
|**dataSetMappingStatus** | [**DataSetMappingStatusEnum**](#DataSetMappingStatusEnum) | Gets the status of the data set mapping. |  [optional] [readonly] |
|**databaseName** | **String** | DatabaseName name of the sink data set |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the data set mapping. |  [optional] [readonly] |
|**schemaName** | **String** | Schema of the table. Default value is dbo. |  |
|**sqlServerResourceId** | **String** | Resource id of SQL server |  |
|**tableName** | **String** | SQL DB table name. |  |



## Enum: DataSetMappingStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;Ok&quot; |
| BROKEN | &quot;Broken&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



