

# GoogleCloudChannelV1alpha1ReportStatus

Status of a report generation process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The report generation&#39;s completion time. |  [optional] |
|**startTime** | **String** | The report generation&#39;s start time. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the report generation process. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STARTED | &quot;STARTED&quot; |
| WRITING | &quot;WRITING&quot; |
| AVAILABLE | &quot;AVAILABLE&quot; |
| FAILED | &quot;FAILED&quot; |



