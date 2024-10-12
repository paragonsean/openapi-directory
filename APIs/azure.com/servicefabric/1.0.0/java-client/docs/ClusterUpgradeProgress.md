

# ClusterUpgradeProgress

The progress of the cluster upgrade

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeVersion** | **String** |  |  [optional] |
|**configVersion** | **String** |  |  [optional] |
|**currentUpgradeDomainProgress** | [**ApplicationUpgradeCurrentUpgradeDomainProgress**](ApplicationUpgradeCurrentUpgradeDomainProgress.md) |  |  [optional] |
|**failureReason** | **FailureReason** |  |  [optional] |
|**failureTimestampUtc** | **String** |  |  [optional] |
|**nextUpgradeDomain** | **String** |  |  [optional] |
|**rollingUpgradeMode** | **RollingUpgradeMode** |  |  [optional] |
|**startTimestampUtc** | **String** |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;UnhealthyEvaluation&gt;**](UnhealthyEvaluation.md) |  |  [optional] |
|**upgradeDomainDurationInMilliseconds** | **String** |  |  [optional] |
|**upgradeDomainProgressAtFailure** | [**ClusterUpgradeProgressUpgradeDomainProgressAtFailure**](ClusterUpgradeProgressUpgradeDomainProgressAtFailure.md) |  |  [optional] |
|**upgradeDomains** | **List&lt;String&gt;** |  |  [optional] |
|**upgradeDurationInMilliseconds** | **String** |  |  [optional] |
|**upgradeState** | **UpgradeState** |  |  [optional] |



