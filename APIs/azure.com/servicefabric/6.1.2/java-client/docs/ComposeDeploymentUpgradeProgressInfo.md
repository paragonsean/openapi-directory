

# ComposeDeploymentUpgradeProgressInfo

Describes the parameters for a compose deployment upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md) |  |  [optional] |
|**applicationName** | **String** | The name of the target application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**applicationUnhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**applicationUpgradeStatusDetails** | **String** | Additional details of application upgrade including failure message. |  [optional] |
|**currentUpgradeDomainDuration** | **String** | The estimated amount of time spent processing current Upgrade Domain. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**currentUpgradeDomainProgress** | [**CurrentUpgradeDomainProgressInfo**](CurrentUpgradeDomainProgressInfo.md) |  |  [optional] |
|**deploymentName** | **String** | The name of the target deployment. |  [optional] |
|**failureReason** | **FailureReason** |  |  [optional] |
|**failureTimestampUtc** | **String** | The estimated UTC datetime when the upgrade failed and FailureAction was executed. |  [optional] |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**startTimestampUtc** | **String** | The estimated UTC datetime when the upgrade started. |  [optional] |
|**targetApplicationTypeVersion** | **String** | The target application type version (found in the application manifest) for the application upgrade. |  [optional] |
|**upgradeDomainProgressAtFailure** | [**FailureUpgradeDomainProgressInfo**](FailureUpgradeDomainProgressInfo.md) |  |  [optional] |
|**upgradeDuration** | **String** | The estimated amount of time that the overall upgrade elapsed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**upgradeKind** | **UpgradeKind** |  |  [optional] |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |
|**upgradeState** | **ComposeDeploymentUpgradeState** |  |  [optional] |
|**upgradeStatusDetails** | **String** | Additional detailed information about the status of the pending upgrade. |  [optional] |



