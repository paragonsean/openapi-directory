

# AzureWorkloadContainer

Container for the workloads running inside Azure Compute or Classic Compute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureWorkloadContainerExtendedInfo**](AzureWorkloadContainerExtendedInfo.md) |  |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | Time stamp when this container was updated. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | Re-Do Operation |  [optional] |
|**sourceResourceId** | **String** | ARM ID of the virtual machine represented by this Azure Workload Container |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | Workload type for which registration was sent. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| REGISTER | &quot;Register&quot; |
| REREGISTER | &quot;Reregister&quot; |



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
| SQL_DATA_BASE | &quot;SQLDataBase&quot; |
| AZURE_FILE_SHARE | &quot;AzureFileShare&quot; |
| SAP_HANA_DATABASE | &quot;SAPHanaDatabase&quot; |
| SAP_ASE_DATABASE | &quot;SAPAseDatabase&quot; |



