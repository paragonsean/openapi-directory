

# DetectorAbnormalTimePeriod

Class representing Abnormal Time Period detected.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of the correlated event |  [optional] |
|**message** | **String** | Message describing the event |  [optional] |
|**metaData** | **List&lt;List&lt;AnalysisDataDataInnerInner&gt;&gt;** | Downtime metadata |  [optional] |
|**priority** | **Double** | Represents the rank of the Detector |  [optional] |
|**solutions** | [**List&lt;Solution&gt;**](Solution.md) | List of proposed solutions |  [optional] |
|**source** | **String** | Represents the name of the Detector |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the correlated event |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Represents the type of the Detector |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SERVICE_INCIDENT | &quot;ServiceIncident&quot; |
| APP_DEPLOYMENT | &quot;AppDeployment&quot; |
| APP_CRASH | &quot;AppCrash&quot; |
| RUNTIME_ISSUE_DETECTED | &quot;RuntimeIssueDetected&quot; |
| ASE_DEPLOYMENT | &quot;AseDeployment&quot; |
| USER_ISSUE | &quot;UserIssue&quot; |
| PLATFORM_ISSUE | &quot;PlatformIssue&quot; |
| OTHER | &quot;Other&quot; |



