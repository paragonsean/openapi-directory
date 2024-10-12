# CloudBillingApi.CostScenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitments** | [**[Commitment]**](Commitment.md) | New commitments to estimate the costs for. The cost of the commitments will be included in the estimate result and discounts the commitment entitles will be included in the workload cost estimates. A maximum of 100 workloads can be provided. | [optional] 
**scenarioConfig** | [**ScenarioConfig**](ScenarioConfig.md) |  | [optional] 
**workloads** | [**[Workload]**](Workload.md) | The Google Cloud usage whose costs are estimated. A maximum of 100 workloads can be provided. | [optional] 


