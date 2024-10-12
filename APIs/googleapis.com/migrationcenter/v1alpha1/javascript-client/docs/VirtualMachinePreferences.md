# MigrationCenterApi.VirtualMachinePreferences

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitmentPlan** | **String** | Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with. | [optional] 
**computeEnginePreferences** | [**ComputeEnginePreferences**](ComputeEnginePreferences.md) |  | [optional] 
**networkCostParameters** | [**VirtualMachinePreferencesNetworkCostParameters**](VirtualMachinePreferencesNetworkCostParameters.md) |  | [optional] 
**regionPreferences** | [**RegionPreferences**](RegionPreferences.md) |  | [optional] 
**sizingOptimizationCustomParameters** | [**VirtualMachinePreferencesSizingOptimizationCustomParameters**](VirtualMachinePreferencesSizingOptimizationCustomParameters.md) |  | [optional] 
**sizingOptimizationStrategy** | **String** | Sizing optimization strategy specifies the preferred strategy used when extrapolating usage data to calculate insights and recommendations for a virtual machine. If you are unsure which value to set, a moderate sizing optimization strategy is often a good value to start with. | [optional] 
**soleTenancyPreferences** | [**SoleTenancyPreferences**](SoleTenancyPreferences.md) |  | [optional] 
**targetProduct** | **String** | Target product for assets using this preference set. Specify either target product or business goal, but not both. | [optional] 
**vmwareEnginePreferences** | [**VmwareEnginePreferences**](VmwareEnginePreferences.md) |  | [optional] 



## Enum: CommitmentPlanEnum


* `UNSPECIFIED` (value: `"COMMITMENT_PLAN_UNSPECIFIED"`)

* `NONE` (value: `"COMMITMENT_PLAN_NONE"`)

* `ONE_YEAR` (value: `"COMMITMENT_PLAN_ONE_YEAR"`)

* `THREE_YEARS` (value: `"COMMITMENT_PLAN_THREE_YEARS"`)





## Enum: SizingOptimizationStrategyEnum


* `UNSPECIFIED` (value: `"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED"`)

* `SAME_AS_SOURCE` (value: `"SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE"`)

* `MODERATE` (value: `"SIZING_OPTIMIZATION_STRATEGY_MODERATE"`)

* `AGGRESSIVE` (value: `"SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE"`)

* `CUSTOM` (value: `"SIZING_OPTIMIZATION_STRATEGY_CUSTOM"`)





## Enum: TargetProductEnum


* `UNSPECIFIED` (value: `"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"`)

* `COMPUTE_ENGINE` (value: `"COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE"`)

* `VMWARE_ENGINE` (value: `"COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE"`)

* `SOLE_TENANCY` (value: `"COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY"`)




