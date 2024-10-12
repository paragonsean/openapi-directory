

# ImportError

The import error details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithmStepType** | [**AlgorithmStepTypeEnum**](#AlgorithmStepTypeEnum) | The operation type specific  to error reporting. |  [optional] |
|**changeNotReimported** | [**ChangeNotReimported**](ChangeNotReimported.md) |  |  [optional] |
|**connectorId** | **String** | The connector Id. |  [optional] |
|**csObjectId** | **String** | The object Id. |  [optional] |
|**dn** | **String** | The distinguished name. |  [optional] |
|**extensionErrorInfo** | [**ExtensionErrorInfo**](ExtensionErrorInfo.md) |  |  [optional] |
|**id** | **String** | The error Id. |  [optional] |
|**retryCount** | **Integer** | The retry count. |  [optional] |
|**ruleErrorInfo** | [**RuleErrorInfo**](RuleErrorInfo.md) |  |  [optional] |
|**runStepResultId** | **String** | The run step result Id. |  [optional] |
|**timeFirstOccurred** | **OffsetDateTime** | The time when the import error first occurred. |  [optional] |
|**timeOccurred** | **OffsetDateTime** | The time when the import error occurred. |  [optional] |
|**type** | **String** | The type of error. |  [optional] |



## Enum: AlgorithmStepTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| STAGING | &quot;Staging&quot; |
| CONNECTOR_FILTER | &quot;ConnectorFilter&quot; |
| JOIN | &quot;Join&quot; |
| PROJECTION | &quot;Projection&quot; |
| IMPORT_FLOW | &quot;ImportFlow&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| VALIDATE_CONNECTOR_FILTER | &quot;ValidateConnectorFilter&quot; |
| DEPROVISIONING | &quot;Deprovisioning&quot; |
| EXPORT_FLOW | &quot;ExportFlow&quot; |
| MV_DELETION | &quot;MvDeletion&quot; |
| RECALL | &quot;Recall&quot; |
| MV_OBJECT_TYPE_CHANGE | &quot;MvObjectTypeChange&quot; |



