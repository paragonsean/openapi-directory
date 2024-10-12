# SiteRecoveryManagementClient.RecoveryPlanAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionName** | **String** | The action name. | 
**customDetails** | [**RecoveryPlanActionDetails**](RecoveryPlanActionDetails.md) |  | 
**failoverDirections** | **[String]** | The list of failover directions. | 
**failoverTypes** | **[String]** | The list of failover types. | 



## Enum: [FailoverDirectionsEnum]


* `PrimaryToRecovery` (value: `"PrimaryToRecovery"`)

* `RecoveryToPrimary` (value: `"RecoveryToPrimary"`)





## Enum: [FailoverTypesEnum]


* `ReverseReplicate` (value: `"ReverseReplicate"`)

* `Commit` (value: `"Commit"`)

* `PlannedFailover` (value: `"PlannedFailover"`)

* `UnplannedFailover` (value: `"UnplannedFailover"`)

* `DisableProtection` (value: `"DisableProtection"`)

* `TestFailover` (value: `"TestFailover"`)

* `TestFailoverCleanup` (value: `"TestFailoverCleanup"`)

* `Failback` (value: `"Failback"`)

* `FinalizeFailback` (value: `"FinalizeFailback"`)

* `ChangePit` (value: `"ChangePit"`)

* `RepairReplication` (value: `"RepairReplication"`)

* `SwitchProtection` (value: `"SwitchProtection"`)

* `CompleteMigration` (value: `"CompleteMigration"`)




