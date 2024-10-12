

# GenericProtectedItem

Base class for backup items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fabricName** | **String** | Name of this backup item&#39;s fabric. |  [optional] |
|**friendlyName** | **String** | Friendly name of the container. |  [optional] |
|**policyState** | **String** | Indicates consistency of policy object and policy applied to this backup item. |  [optional] |
|**protectedItemId** | **Long** | Data Plane Service ID of the protected item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of this backup item. |  [optional] |
|**sourceAssociations** | **Map&lt;String, String&gt;** | Loosely coupled (type, value) associations (example - parent of a protected item) |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



