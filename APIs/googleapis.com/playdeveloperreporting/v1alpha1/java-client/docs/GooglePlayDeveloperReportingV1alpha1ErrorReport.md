

# GooglePlayDeveloperReportingV1alpha1ErrorReport

An error report received for an app. There reports are produced by the Android platform code when a (potentially fatal) error condition is detected. Identical reports from many users will be deduplicated and coalesced into a single ErrorReport. **Required permissions**: to access this resource, the calling user needs the _View app information (read-only)_ permission for the app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appVersion** | [**GooglePlayDeveloperReportingV1alpha1AppVersion**](GooglePlayDeveloperReportingV1alpha1AppVersion.md) |  |  [optional] |
|**deviceModel** | [**GooglePlayDeveloperReportingV1alpha1DeviceModelSummary**](GooglePlayDeveloperReportingV1alpha1DeviceModelSummary.md) |  |  [optional] |
|**eventTime** | **String** | Start of the hour during which the latest event in this error report occurred. |  [optional] |
|**issue** | **String** | The issue this report was associated with. **Please note:** this resource is currently in Alpha. There could be changes to the issue grouping that would result in similar but more recent error reports being assigned to a different issue. |  [optional] |
|**name** | **String** | The resource name of the report. Format: apps/{app}/{report} |  [optional] |
|**osVersion** | [**GooglePlayDeveloperReportingV1alpha1OsVersion**](GooglePlayDeveloperReportingV1alpha1OsVersion.md) |  |  [optional] |
|**reportText** | **String** | Textual representation of the error report. These textual reports are produced by the platform. The reports are then sanitized and filtered to remove any potentially sensitive information. Although their format is fairly stable, they are not entirely meant for machine consumption and we cannot guarantee that there won&#39;t be subtle changes to the formatting that may break systems trying to parse information out of the reports. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the error for which this report was generated. |  [optional] |
|**vcsInformation** | **String** | Version control system information from BUNDLE-METADATA/version-control-info.textproto or META-INF/version-control-info.textproto of the app bundle or APK, respectively. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ERROR_TYPE_UNSPECIFIED | &quot;ERROR_TYPE_UNSPECIFIED&quot; |
| APPLICATION_NOT_RESPONDING | &quot;APPLICATION_NOT_RESPONDING&quot; |
| CRASH | &quot;CRASH&quot; |



