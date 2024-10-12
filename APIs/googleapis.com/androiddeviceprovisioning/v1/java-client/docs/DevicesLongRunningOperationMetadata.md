

# DevicesLongRunningOperationMetadata

Tracks the status of a long-running operation to asynchronously update a batch of reseller metadata attached to devices. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devicesCount** | **Integer** | The number of metadata updates in the operation. This might be different from the number of updates in the request if the API can&#39;t parse some of the updates. |  [optional] |
|**processingStatus** | [**ProcessingStatusEnum**](#ProcessingStatusEnum) | The processing status of the operation. |  [optional] |
|**progress** | **Integer** | The processing progress of the operation. Measured as a number from 0 to 100. A value of 10O doesn&#39;t always mean the operation completed—check for the inclusion of a &#x60;done&#x60; field. |  [optional] |



## Enum: ProcessingStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;BATCH_PROCESS_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;BATCH_PROCESS_PENDING&quot; |
| IN_PROGRESS | &quot;BATCH_PROCESS_IN_PROGRESS&quot; |
| PROCESSED | &quot;BATCH_PROCESS_PROCESSED&quot; |



