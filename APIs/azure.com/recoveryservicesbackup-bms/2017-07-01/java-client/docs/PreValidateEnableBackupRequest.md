

# PreValidateEnableBackupRequest

Contract to validate if backup can be enabled on the given resource in a given vault and given configuration.  It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | **String** | Configuration of VM if any needs to be validated like OS type etc |  [optional] |
|**resourceId** | **String** | ARM Virtual Machine Id |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | ProtectedItem Type- VM, SqlDataBase, AzureFileShare etc |  [optional] |
|**vaultId** | **String** | ARM id of the Recovery Services Vault |  [optional] |



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



