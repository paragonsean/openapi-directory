

# AzureVmWorkloadProtectionPolicy

Azure VM (Mercury) workload-specific backup policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**makePolicyConsistent** | **Boolean** | Fix the policy inconsistency |  [optional] |
|**settings** | [**Settings**](Settings.md) |  |  [optional] |
|**subProtectionPolicy** | [**List&lt;SubProtectionPolicy&gt;**](SubProtectionPolicy.md) | List of sub-protection policies which includes schedule and retention |  [optional] |
|**workLoadType** | [**WorkLoadTypeEnum**](#WorkLoadTypeEnum) | Type of workload for the backup management |  [optional] |



## Enum: WorkLoadTypeEnum

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



