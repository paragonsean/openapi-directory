

# BuildGroup

Contains information about a batch build build group. Build groups are used to combine builds that can run in parallel, while still being able to set dependencies on other build groups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identifier** | [**String**](String.md) |  |  [optional] |
|**dependsOn** | [**List**](List.md) |  |  [optional] |
|**ignoreFailure** | [**Boolean**](Boolean.md) |  |  [optional] |
|**currentBuildSummary** | [**BuildGroupCurrentBuildSummary**](BuildGroupCurrentBuildSummary.md) |  |  [optional] |
|**priorBuildSummaryList** | [**List**](List.md) |  |  [optional] |



