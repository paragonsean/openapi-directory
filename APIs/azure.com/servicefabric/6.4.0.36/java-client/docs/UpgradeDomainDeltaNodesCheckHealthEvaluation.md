

# UpgradeDomainDeltaNodesCheckHealthEvaluation

Represents health evaluation for delta unhealthy cluster nodes in an upgrade domain, containing health evaluations for each unhealthy node that impacted current aggregated health state. Can be returned during cluster upgrade when cluster aggregated health state is Warning or Error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baselineErrorCount** | **Long** | Number of upgrade domain nodes with aggregated heath state Error in the health store at the beginning of the cluster upgrade. |  [optional] |
|**baselineTotalCount** | **Long** | Total number of upgrade domain nodes in the health store at the beginning of the cluster upgrade. |  [optional] |
|**maxPercentDeltaUnhealthyNodes** | **Integer** | Maximum allowed percentage of upgrade domain delta unhealthy nodes from the ClusterUpgradeHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of upgrade domain nodes in the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**upgradeDomainName** | **String** | Name of the upgrade domain where nodes health is currently evaluated. |  [optional] |



