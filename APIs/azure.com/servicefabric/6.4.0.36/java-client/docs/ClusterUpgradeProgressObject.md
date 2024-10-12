

# ClusterUpgradeProgressObject

Information about a cluster upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeVersion** | **String** | The ServiceFabric code version of the cluster. |  [optional] |
|**configVersion** | **String** | The cluster configuration version (specified in the cluster manifest). |  [optional] |
|**currentUpgradeDomainProgress** | [**CurrentUpgradeDomainProgressInfo**](CurrentUpgradeDomainProgressInfo.md) |  |  [optional] |
|**failureReason** | **FailureReason** |  |  [optional] |
|**failureTimestampUtc** | **String** | The failure time of the upgrade in UTC. |  [optional] |
|**nextUpgradeDomain** | **String** | The name of the next upgrade domain to be processed. |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**startTimestampUtc** | **String** | The start time of the upgrade in UTC. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**upgradeDescription** | [**ClusterUpgradeDescriptionObject**](ClusterUpgradeDescriptionObject.md) |  |  [optional] |
|**upgradeDomainDurationInMilliseconds** | **String** | The estimated elapsed time spent processing the current upgrade domain. |  [optional] |
|**upgradeDomainProgressAtFailure** | [**FailedUpgradeDomainProgressObject**](FailedUpgradeDomainProgressObject.md) |  |  [optional] |
|**upgradeDomains** | [**List&lt;UpgradeDomainInfo&gt;**](UpgradeDomainInfo.md) | List of upgrade domains and their statuses. |  [optional] |
|**upgradeDurationInMilliseconds** | **String** | The estimated elapsed time spent processing the current overall upgrade. |  [optional] |
|**upgradeState** | **UpgradeState** |  |  [optional] |



