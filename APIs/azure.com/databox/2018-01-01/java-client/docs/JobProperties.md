

# JobProperties

Job Properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationReason** | **String** | Reason for cancellation. |  [optional] [readonly] |
|**details** | [**JobDetails**](JobDetails.md) |  |  [optional] |
|**error** | [**Error**](Error.md) |  |  [optional] |
|**isCancellable** | **Boolean** | Describes whether the job is cancellable or not. |  [optional] [readonly] |
|**isDeletable** | **Boolean** | Describes whether the job is deletable or not. |  [optional] [readonly] |
|**isShippingAddressEditable** | **Boolean** | Describes whether the shipping address is editable or not. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Time at which the job was started in UTC ISO 8601 format. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Name of the stage which is in progress. |  [optional] [readonly] |



## Enum: StatusEnum

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



