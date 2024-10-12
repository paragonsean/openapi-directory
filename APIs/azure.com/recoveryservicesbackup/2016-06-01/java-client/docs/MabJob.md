

# MabJob

The Azure Backup Server workload-specific job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsInfo** | [**List&lt;ActionsInfoEnum&gt;**](#List&lt;ActionsInfoEnum&gt;) | The state or actions applicable on jobs such as Cancel or Retry. |  [optional] |
|**duration** | **String** | The time required for the job to run. |  [optional] |
|**errorDetails** | [**List&lt;MabErrorInfo&gt;**](MabErrorInfo.md) | The errors. |  [optional] |
|**extendedInfo** | [**MabJobExtendedInfo**](MabJobExtendedInfo.md) |  |  [optional] |
|**mabServerName** | **String** | The name of server protecting the data store. |  [optional] |
|**mabServerType** | [**MabServerTypeEnum**](#MabServerTypeEnum) | Server type of the Azure Backup Server container. |  [optional] |
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
| DPM_VENUS_CONTAINER | &quot;DPMVenusContainer&quot; |
| MAB_CONTAINER | &quot;MABContainer&quot; |
| CLUSTER_RESOURCE | &quot;ClusterResource&quot; |
| AZURE_SQL_CONTAINER | &quot;AzureSqlContainer&quot; |
| WINDOWS_SERVER | &quot;WindowsServer&quot; |
| WINDOWS | &quot;Windows&quot; |



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
| DPM_UNKNOWN | &quot;DPMUnknown&quot; |



