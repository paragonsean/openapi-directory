# ServiceFabricClientApis.MonitoringPolicyDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureAction** | [**FailureAction**](FailureAction.md) |  | [optional] 
**healthCheckRetryTimeoutInMilliseconds** | **String** | The amount of time to retry health evaluation when the application or cluster is unhealthy before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;PT0H10M0S&#39;]
**healthCheckStableDurationInMilliseconds** | **String** | The amount of time that the application or cluster must remain healthy before the upgrade proceeds to the next upgrade domain. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;PT0H2M0S&#39;]
**healthCheckWaitDurationInMilliseconds** | **String** | The amount of time to wait after completing an upgrade domain before applying health policies. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;0&#39;]
**upgradeDomainTimeoutInMilliseconds** | **String** | The amount of time each upgrade domain has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;P10675199DT02H48M05.4775807S&#39;]
**upgradeTimeoutInMilliseconds** | **String** | The amount of time the overall upgrade has to complete before FailureAction is executed. It is first interpreted as a string representing an ISO 8601 duration. If that fails, then it is interpreted as a number representing the total number of milliseconds. | [optional] [default to &#39;P10675199DT02H48M05.4775807S&#39;]


