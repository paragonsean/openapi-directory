

# MonitoringPolicyDescription

Describes the parameters for monitoring an upgrade in Monitored mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureAction** | **FailureAction** |  |  [optional] |
|**healthCheckRetryTimeoutInMilliseconds** | **String** | The amount of time to retry health evaluation when the application or cluster is unhealthy before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**healthCheckStableDurationInMilliseconds** | **String** | The amount of time that the application or cluster must remain healthy before the upgrade proceeds to the next upgrade domain. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**healthCheckWaitDurationInMilliseconds** | **String** | The amount of time to wait after completing an upgrade domain before applying health policies. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**upgradeDomainTimeoutInMilliseconds** | **String** | The amount of time each upgrade domain has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |
|**upgradeTimeoutInMilliseconds** | **String** | The amount of time the overall upgrade has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. |  [optional] |



