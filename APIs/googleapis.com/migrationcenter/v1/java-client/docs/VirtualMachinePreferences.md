

# VirtualMachinePreferences

VirtualMachinePreferences enables you to create sets of assumptions, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentPlan** | [**CommitmentPlanEnum**](#CommitmentPlanEnum) | Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with. |  [optional] |
|**computeEnginePreferences** | [**ComputeEnginePreferences**](ComputeEnginePreferences.md) |  |  [optional] |
|**regionPreferences** | [**RegionPreferences**](RegionPreferences.md) |  |  [optional] |
|**sizingOptimizationStrategy** | [**SizingOptimizationStrategyEnum**](#SizingOptimizationStrategyEnum) | Sizing optimization strategy specifies the preferred strategy used when extrapolating usage data to calculate insights and recommendations for a virtual machine. If you are unsure which value to set, a moderate sizing optimization strategy is often a good value to start with. |  [optional] |
|**soleTenancyPreferences** | [**SoleTenancyPreferences**](SoleTenancyPreferences.md) |  |  [optional] |
|**targetProduct** | [**TargetProductEnum**](#TargetProductEnum) | Target product for assets using this preference set. Specify either target product or business goal, but not both. |  [optional] |
|**vmwareEnginePreferences** | [**VmwareEnginePreferences**](VmwareEnginePreferences.md) |  |  [optional] |



## Enum: CommitmentPlanEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;COMMITMENT_PLAN_UNSPECIFIED&quot; |
| NONE | &quot;COMMITMENT_PLAN_NONE&quot; |
| ONE_YEAR | &quot;COMMITMENT_PLAN_ONE_YEAR&quot; |
| THREE_YEARS | &quot;COMMITMENT_PLAN_THREE_YEARS&quot; |



## Enum: SizingOptimizationStrategyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED&quot; |
| SAME_AS_SOURCE | &quot;SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE&quot; |
| MODERATE | &quot;SIZING_OPTIMIZATION_STRATEGY_MODERATE&quot; |
| AGGRESSIVE | &quot;SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE&quot; |



## Enum: TargetProductEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED&quot; |
| COMPUTE_ENGINE | &quot;COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE&quot; |
| VMWARE_ENGINE | &quot;COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE&quot; |
| SOLE_TENANCY | &quot;COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY&quot; |



