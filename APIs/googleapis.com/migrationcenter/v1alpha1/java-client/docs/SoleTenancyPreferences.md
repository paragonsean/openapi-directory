

# SoleTenancyPreferences

Preferences concerning Sole Tenancy nodes and VMs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentPlan** | [**CommitmentPlanEnum**](#CommitmentPlanEnum) | Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with. |  [optional] |
|**cpuOvercommitRatio** | **Double** | CPU overcommit ratio. Acceptable values are between 1.0 and 2.0 inclusive. |  [optional] |
|**hostMaintenancePolicy** | [**HostMaintenancePolicyEnum**](#HostMaintenancePolicyEnum) | Sole Tenancy nodes maintenance policy. |  [optional] |
|**nodeTypes** | [**List&lt;SoleTenantNodeType&gt;**](SoleTenantNodeType.md) | A list of sole tenant node types. An empty list means that all possible node types will be considered. |  [optional] |



## Enum: CommitmentPlanEnum

| Name | Value |
|---- | -----|
| COMMITMENT_PLAN_UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |
| COMMITMENT_1_YEAR | &quot;COMMITMENT_1_YEAR&quot; |
| COMMITMENT_3_YEAR | &quot;COMMITMENT_3_YEAR&quot; |



## Enum: HostMaintenancePolicyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HOST_MAINTENANCE_POLICY_UNSPECIFIED&quot; |
| DEFAULT | &quot;HOST_MAINTENANCE_POLICY_DEFAULT&quot; |
| RESTART_IN_PLACE | &quot;HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE&quot; |
| MIGRATE_WITHIN_NODE_GROUP | &quot;HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP&quot; |



