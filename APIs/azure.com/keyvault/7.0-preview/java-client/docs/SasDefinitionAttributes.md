

# SasDefinitionAttributes

The SAS definition management attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **Integer** | Creation time in UTC. |  [optional] [readonly] |
|**enabled** | **Boolean** | the enabled state of the object. |  [optional] |
|**recoveryLevel** | [**RecoveryLevelEnum**](#RecoveryLevelEnum) | Reflects the deletion recovery level currently in effect for SAS definitions in the current vault. If it contains &#39;Purgeable&#39; the SAS definition can be permanently deleted by a privileged user; otherwise, only the system can purge the SAS definition, at the end of the retention interval. |  [optional] [readonly] |
|**updated** | **Integer** | Last updated time in UTC. |  [optional] [readonly] |



## Enum: RecoveryLevelEnum

| Name | Value |
|---- | -----|
| PURGEABLE | &quot;Purgeable&quot; |
| RECOVERABLE_PURGEABLE | &quot;Recoverable+Purgeable&quot; |
| RECOVERABLE | &quot;Recoverable&quot; |
| RECOVERABLE_PROTECTED_SUBSCRIPTION | &quot;Recoverable+ProtectedSubscription&quot; |



