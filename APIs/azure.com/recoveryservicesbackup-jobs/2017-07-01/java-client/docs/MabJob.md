

# MabJob

MAB workload-specific job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | The state/actions applicable on jobs like cancel/retry. |  [optional] |
|**duration** | **String** | Time taken by job to run. |  [optional] |
|**errorDetails** | [**List&lt;MabErrorInfo&gt;**](MabErrorInfo.md) | The errors. |  [optional] |
|**extendedInfo** | [**MabJobExtendedInfo**](MabJobExtendedInfo.md) |  |  [optional] |
|**mabServerName** | **String** | Name of server protecting the DS. |  [optional] |
|**mabServerType** | [**MabServerTypeEnum**](#MabServerTypeEnum) | Server type of MAB container. |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | Workload type of backup item. |  [optional] |



## Enum: List&lt;ActionsInfoEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |
| RETRIABLE | &quot;Retriable&quot; |



## Enum: MabServerTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| IAAS_VM_CONTAINER | &quot;IaasVMContainer&quot; |
| IAAS_VM_SERVICE_CONTAINER | &quot;IaasVMServiceContainer&quot; |
| DPM_CONTAINER | &quot;DPMContainer&quot; |
| AZURE_BACKUP_SERVER_CONTAINER | &quot;AzureBackupServerContainer&quot; |
| MAB_CONTAINER | &quot;MABContainer&quot; |
| CLUSTER | &quot;Cluster&quot; |
| AZURE_SQL_CONTAINER | &quot;AzureSqlContainer&quot; |
| WINDOWS | &quot;Windows&quot; |
| V_CENTER | &quot;VCenter&quot; |



## Enum: WorkloadTypeEnum

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



