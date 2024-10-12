

# GooglePlayDeveloperReportingV1alpha1ErrorIssue

A group of related ErrorReports received for an app. Similar error reports are grouped together into issues with a likely identical root cause. **Please note:** this resource is currently in Alpha. There could be changes to the issue grouping that would result in similar but more recent error reports being assigned to different issues. This could also cause some issues disappearing entirely and being replaced by new ones. **Required permissions**: to access this resource, the calling user needs the _View app information (read-only)_ permission for the app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cause** | **String** | Cause of the issue. Depending on the type this can be either: * APPLICATION_NOT_RESPONDING: the type of ANR that occurred, e.g., &#39;Input dispatching timed out&#39;. * CRASH: for Java unhandled exception errors, the type of the innermost exception that was thrown, e.g., IllegalArgumentException. For signals in native code, the signal that was raised, e.g. SIGSEGV. |  [optional] |
|**distinctUsers** | **String** | An estimate of the number of unique users who have experienced this issue (only considering occurrences matching the filters and within the requested time period). |  [optional] |
|**distinctUsersPercent** | [**GoogleTypeDecimal**](GoogleTypeDecimal.md) |  |  [optional] |
|**errorReportCount** | **String** | The total number of error reports in this issue (only considering occurrences matching the filters and within the requested time period). |  [optional] |
|**firstAppVersion** | [**GooglePlayDeveloperReportingV1alpha1AppVersion**](GooglePlayDeveloperReportingV1alpha1AppVersion.md) |  |  [optional] |
|**firstOsVersion** | [**GooglePlayDeveloperReportingV1alpha1OsVersion**](GooglePlayDeveloperReportingV1alpha1OsVersion.md) |  |  [optional] |
|**issueUri** | **String** | Link to the issue in Android vitals in the Play Console. |  [optional] |
|**lastAppVersion** | [**GooglePlayDeveloperReportingV1alpha1AppVersion**](GooglePlayDeveloperReportingV1alpha1AppVersion.md) |  |  [optional] |
|**lastErrorReportTime** | **String** | Start of the hour during which the last error report in this issue occurred. |  [optional] |
|**lastOsVersion** | [**GooglePlayDeveloperReportingV1alpha1OsVersion**](GooglePlayDeveloperReportingV1alpha1OsVersion.md) |  |  [optional] |
|**location** | **String** | Location where the issue happened. Depending on the type this can be either: * APPLICATION_NOT_RESPONDING: the name of the activity or service that stopped responding. * CRASH: the likely method name that caused the error. |  [optional] |
|**name** | **String** | Identifier. The resource name of the issue. Format: apps/{app}/{issue} |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the errors grouped in this issue. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ERROR_TYPE_UNSPECIFIED | &quot;ERROR_TYPE_UNSPECIFIED&quot; |
| APPLICATION_NOT_RESPONDING | &quot;APPLICATION_NOT_RESPONDING&quot; |
| CRASH | &quot;CRASH&quot; |



