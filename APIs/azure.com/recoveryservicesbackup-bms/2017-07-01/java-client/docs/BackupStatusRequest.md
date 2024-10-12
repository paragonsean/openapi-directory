

# BackupStatusRequest

BackupStatus request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**poLogicalName** | **String** | Protectable Item Logical Name |  [optional] |
|**resourceId** | **String** | Entire ARM resource id of the resource |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | Container Type - VM, SQLPaaS, DPM, AzureFileShare... |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| VM | &quot;VM&quot; |
| FILE_FOLDER | &quot;FileFolder&quot; |
| AZURE_SQL_DB | &quot;AzureSqlDb&quot; |
| SQLDB | &quot;SQLDB&quot; |
| EXCHANGE | &quot;Exchange&quot; |
| SHAREPOINT | &quot;Sharepoint&quot; |
| V_MWARE_VM | &quot;VMwareVM&quot; |
| SYSTEM_STATE | &quot;SystemState&quot; |
| CLIENT | &quot;Client&quot; |
| GENERIC_DATA_SOURCE | &quot;GenericDataSource&quot; |
| SQL_DATA_BASE | &quot;SQLDataBase&quot; |
| AZURE_FILE_SHARE | &quot;AzureFileShare&quot; |
| SAP_HANA_DATABASE | &quot;SAPHanaDatabase&quot; |
| SAP_ASE_DATABASE | &quot;SAPAseDatabase&quot; |



