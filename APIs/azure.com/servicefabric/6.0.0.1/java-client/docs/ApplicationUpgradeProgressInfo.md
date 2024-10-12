

# ApplicationUpgradeProgressInfo

Describes the parameters for an application upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentUpgradeDomainProgress** | [**CurrentUpgradeDomainProgressInfo**](CurrentUpgradeDomainProgressInfo.md) |  |  [optional] |
|**failureReason** | **FailureReason** |  |  [optional] |
|**failureTimestampUtc** | **String** | The estimated UTC datetime when the upgrade failed and FailureAction was executed. |  [optional] |
|**name** | **String** | The name of the target application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**nextUpgradeDomain** | **String** | The name of the next upgrade domain to be processed. |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**startTimestampUtc** | **String** | The estimated UTC datetime when the upgrade started. |  [optional] |
|**targetApplicationTypeVersion** | **String** | The target application type version (found in the application manifest) for the application upgrade. |  [optional] |
|**typeName** | **String** | The application type name as defined in the application manifest. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**upgradeDescription** | [**ApplicationUpgradeDescription**](ApplicationUpgradeDescription.md) |  |  [optional] |
|**upgradeDomainDurationInMilliseconds** | **String** | The estimated total amount of time spent processing the current upgrade domain. |  [optional] |
|**upgradeDomainProgressAtFailure** | [**FailureUpgradeDomainProgressInfo**](FailureUpgradeDomainProgressInfo.md) |  |  [optional] |
|**upgradeDomains** | [**List&lt;UpgradeDomainInfo&gt;**](UpgradeDomainInfo.md) | List of upgrade domains and their statuses. |  [optional] |
|**upgradeDurationInMilliseconds** | **String** | The estimated total amount of time spent processing the overall upgrade. |  [optional] |
|**upgradeState** | **UpgradeState** |  |  [optional] |
|**upgradeStatusDetails** | **String** | Additional detailed information about the status of the pending upgrade. |  [optional] |



