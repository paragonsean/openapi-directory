

# JobStages

Job stages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Display name of the job stage. |  [optional] [readonly] |
|**errorDetails** | [**List&lt;JobErrorDetails&gt;**](JobErrorDetails.md) | Error details for the stage. |  [optional] [readonly] |
|**jobStageDetails** | **Object** | Job Stage Details |  [optional] [readonly] |
|**stageName** | [**StageNameEnum**](#StageNameEnum) | Name of the job stage. |  [optional] [readonly] |
|**stageStatus** | [**StageStatusEnum**](#StageStatusEnum) | Status of the job stage. |  [optional] [readonly] |
|**stageTime** | **OffsetDateTime** | Time for the job stage in UTC ISO 8601 format. |  [optional] [readonly] |



## Enum: StageNameEnum

| Name | Value |
|---- | -----|
| DEVICE_ORDERED | &quot;DeviceOrdered&quot; |
| DEVICE_PREPARED | &quot;DevicePrepared&quot; |
| DISPATCHED | &quot;Dispatched&quot; |
| DELIVERED | &quot;Delivered&quot; |
| PICKED_UP | &quot;PickedUp&quot; |
| AT_AZURE_DC | &quot;AtAzureDC&quot; |
| DATA_COPY | &quot;DataCopy&quot; |
| COMPLETED | &quot;Completed&quot; |
| COMPLETED_WITH_ERRORS | &quot;CompletedWithErrors&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED_ISSUE_REPORTED_AT_CUSTOMER | &quot;Failed_IssueReportedAtCustomer&quot; |
| FAILED_ISSUE_DETECTED_AT_AZURE_DC | &quot;Failed_IssueDetectedAtAzureDC&quot; |
| ABORTED | &quot;Aborted&quot; |
| COMPLETED_WITH_WARNINGS | &quot;CompletedWithWarnings&quot; |
| READY_TO_DISPATCH_FROM_AZURE_DC | &quot;ReadyToDispatchFromAzureDC&quot; |
| READY_TO_RECEIVE_AT_AZURE_DC | &quot;ReadyToReceiveAtAzureDC&quot; |



## Enum: StageStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CANCELLING | &quot;Cancelling&quot; |
| SUCCEEDED_WITH_ERRORS | &quot;SucceededWithErrors&quot; |



