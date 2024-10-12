# MigrationCenterApi.SoleTenancyPreferences

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitmentPlan** | **String** | Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with. | [optional] 
**cpuOvercommitRatio** | **Number** | CPU overcommit ratio. Acceptable values are between 1.0 and 2.0 inclusive. | [optional] 
**hostMaintenancePolicy** | **String** | Sole Tenancy nodes maintenance policy. | [optional] 
**nodeTypes** | [**[SoleTenantNodeType]**](SoleTenantNodeType.md) | A list of sole tenant node types. An empty list means that all possible node types will be considered. | [optional] 



## Enum: CommitmentPlanEnum


* `COMMITMENT_PLAN_UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `COMMITMENT_1_YEAR` (value: `"COMMITMENT_1_YEAR"`)

* `COMMITMENT_3_YEAR` (value: `"COMMITMENT_3_YEAR"`)





## Enum: HostMaintenancePolicyEnum


* `UNSPECIFIED` (value: `"HOST_MAINTENANCE_POLICY_UNSPECIFIED"`)

* `DEFAULT` (value: `"HOST_MAINTENANCE_POLICY_DEFAULT"`)

* `RESTART_IN_PLACE` (value: `"HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE"`)

* `MIGRATE_WITHIN_NODE_GROUP` (value: `"HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP"`)




