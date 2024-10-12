# ServiceFabricClientApis.RollingUpgradeUpdateDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureAction** | [**FailureAction**](FailureAction.md) |  | [optional] 
**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). | [optional] [default to false]
**healthCheckRetryTimeoutInMilliseconds** | **String** | The amount of time to retry health evaluation when the application or cluster is unhealthy before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;PT0H10M0S&#39;]
**healthCheckStableDurationInMilliseconds** | **String** | The amount of time that the application or cluster must remain healthy before the upgrade proceeds to the next upgrade domain. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;PT0H2M0S&#39;]
**healthCheckWaitDurationInMilliseconds** | **String** | The amount of time to wait after completing an upgrade domain before applying health policies. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;0&#39;]
**instanceCloseDelayDurationInSeconds** | **Number** | Duration in seconds, to wait before a stateless instance is closed, to allow the active requests to drain gracefully. This would be effective when the instance is closing during the application/cluster upgrade, only for those instances which have a non-zero delay duration configured in the service description. See InstanceCloseDelayDurationSeconds property in $ref: \&quot;#/definitions/StatelessServiceDescription.yaml\&quot; for details. Note, the default value of InstanceCloseDelayDurationInSeconds is 4294967295, which indicates that the behavior will entirely depend on the delay configured in the stateless service description. | [optional] 
**replicaSetCheckTimeoutInMilliseconds** | **Number** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). | [optional] 
**rollingUpgradeMode** | [**UpgradeMode**](UpgradeMode.md) |  | 
**upgradeDomainTimeoutInMilliseconds** | **String** | The amount of time each upgrade domain has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;P10675199DT02H48M05.4775807S&#39;]
**upgradeTimeoutInMilliseconds** | **String** | The amount of time the overall upgrade has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;P10675199DT02H48M05.4775807S&#39;]


