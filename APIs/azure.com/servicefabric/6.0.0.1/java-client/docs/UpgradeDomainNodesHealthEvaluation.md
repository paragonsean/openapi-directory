

# UpgradeDomainNodesHealthEvaluation

Represents health evaluation for cluster nodes in an upgrade domain, containing health evaluations for each unhealthy node that impacted current aggregated health state. Can be returned when evaluating cluster health during cluster upgrade and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyNodes** | **Integer** | Maximum allowed percentage of unhealthy nodes from the ClusterHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of nodes in the current upgrade domain. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**upgradeDomainName** | **String** | Name of the upgrade domain where nodes health is currently evaluated. |  [optional] |



