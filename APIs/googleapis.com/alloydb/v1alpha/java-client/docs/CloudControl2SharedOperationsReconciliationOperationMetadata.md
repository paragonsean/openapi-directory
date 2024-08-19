

# CloudControl2SharedOperationsReconciliationOperationMetadata

Operation metadata returned by the CLH during resource state reconciliation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deleteResource** | **Boolean** | DEPRECATED. Use exclusive_action instead. |  [optional] |
|**exclusiveAction** | [**ExclusiveActionEnum**](#ExclusiveActionEnum) | Excluisive action returned by the CLH. |  [optional] |



## Enum: ExclusiveActionEnum

| Name | Value |
|---- | -----|
| UNKNOWN_REPAIR_ACTION | &quot;UNKNOWN_REPAIR_ACTION&quot; |
| DELETE | &quot;DELETE&quot; |
| RETRY | &quot;RETRY&quot; |



