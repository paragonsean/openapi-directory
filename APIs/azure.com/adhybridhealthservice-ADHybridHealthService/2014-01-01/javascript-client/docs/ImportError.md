# AdHybridHealthService.ImportError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithmStepType** | **String** | The operation type specific  to error reporting. | [optional] 
**changeNotReimported** | [**ChangeNotReimported**](ChangeNotReimported.md) |  | [optional] 
**connectorId** | **String** | The connector Id. | [optional] 
**csObjectId** | **String** | The object Id. | [optional] 
**dn** | **String** | The distinguished name. | [optional] 
**extensionErrorInfo** | [**ExtensionErrorInfo**](ExtensionErrorInfo.md) |  | [optional] 
**id** | **String** | The error Id. | [optional] 
**retryCount** | **Number** | The retry count. | [optional] 
**ruleErrorInfo** | [**RuleErrorInfo**](RuleErrorInfo.md) |  | [optional] 
**runStepResultId** | **String** | The run step result Id. | [optional] 
**timeFirstOccurred** | **Date** | The time when the import error first occurred. | [optional] 
**timeOccurred** | **Date** | The time when the import error occurred. | [optional] 
**type** | **String** | The type of error. | [optional] 



## Enum: AlgorithmStepTypeEnum


* `Undefined` (value: `"Undefined"`)

* `Staging` (value: `"Staging"`)

* `ConnectorFilter` (value: `"ConnectorFilter"`)

* `Join` (value: `"Join"`)

* `Projection` (value: `"Projection"`)

* `ImportFlow` (value: `"ImportFlow"`)

* `Provisioning` (value: `"Provisioning"`)

* `ValidateConnectorFilter` (value: `"ValidateConnectorFilter"`)

* `Deprovisioning` (value: `"Deprovisioning"`)

* `ExportFlow` (value: `"ExportFlow"`)

* `MvDeletion` (value: `"MvDeletion"`)

* `Recall` (value: `"Recall"`)

* `MvObjectTypeChange` (value: `"MvObjectTypeChange"`)




