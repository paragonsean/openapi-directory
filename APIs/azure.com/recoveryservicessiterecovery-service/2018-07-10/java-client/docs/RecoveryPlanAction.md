

# RecoveryPlanAction

Recovery plan action details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionName** | **String** | The action name. |  |
|**customDetails** | [**RecoveryPlanActionDetails**](RecoveryPlanActionDetails.md) |  |  |
|**failoverDirections** | [**List&lt;FailoverDirectionsEnum&gt;**](#List&lt;FailoverDirectionsEnum&gt;) | The list of failover directions. |  |
|**failoverTypes** | [**List&lt;FailoverTypesEnum&gt;**](#List&lt;FailoverTypesEnum&gt;) | The list of failover types. |  |



## Enum: List&lt;FailoverDirectionsEnum&gt;

| Name | Value |
|---- | -----|
| PRIMARY_TO_RECOVERY | &quot;PrimaryToRecovery&quot; |
| RECOVERY_TO_PRIMARY | &quot;RecoveryToPrimary&quot; |



## Enum: List&lt;FailoverTypesEnum&gt;

| Name | Value |
|---- | -----|
| REVERSE_REPLICATE | &quot;ReverseReplicate&quot; |
| COMMIT | &quot;Commit&quot; |
| PLANNED_FAILOVER | &quot;PlannedFailover&quot; |
| UNPLANNED_FAILOVER | &quot;UnplannedFailover&quot; |
| DISABLE_PROTECTION | &quot;DisableProtection&quot; |
| TEST_FAILOVER | &quot;TestFailover&quot; |
| TEST_FAILOVER_CLEANUP | &quot;TestFailoverCleanup&quot; |
| FAILBACK | &quot;Failback&quot; |
| FINALIZE_FAILBACK | &quot;FinalizeFailback&quot; |
| CHANGE_PIT | &quot;ChangePit&quot; |
| REPAIR_REPLICATION | &quot;RepairReplication&quot; |
| SWITCH_PROTECTION | &quot;SwitchProtection&quot; |
| COMPLETE_MIGRATION | &quot;CompleteMigration&quot; |



