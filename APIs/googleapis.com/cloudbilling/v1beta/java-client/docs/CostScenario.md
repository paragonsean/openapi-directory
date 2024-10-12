

# CostScenario

Encapsulates all the information needed to perform a cost estimate. It includes a specification of the Google Cloud usage whose costs are estimated, and configuration options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitments** | [**List&lt;Commitment&gt;**](Commitment.md) | New commitments to estimate the costs for. The cost of the commitments will be included in the estimate result and discounts the commitment entitles will be included in the workload cost estimates. A maximum of 100 workloads can be provided. |  [optional] |
|**scenarioConfig** | [**ScenarioConfig**](ScenarioConfig.md) |  |  [optional] |
|**workloads** | [**List&lt;Workload&gt;**](Workload.md) | The Google Cloud usage whose costs are estimated. A maximum of 100 workloads can be provided. |  [optional] |



