

# RecommendedActionImplementationInfo

Contains information for manual implementation for an Azure SQL Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | [**MethodEnum**](#MethodEnum) | Gets the method in which this recommended action can be manually implemented. e.g., TSql, AzurePowerShell. |  [optional] [readonly] |
|**script** | **String** | Gets the manual implementation script. e.g., T-SQL script that could be executed on the database. |  [optional] [readonly] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| T_SQL | &quot;TSql&quot; |
| AZURE_POWER_SHELL | &quot;AzurePowerShell&quot; |



