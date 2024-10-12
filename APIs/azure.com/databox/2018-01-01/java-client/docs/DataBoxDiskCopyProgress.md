

# DataBoxDiskCopyProgress

DataBox Disk Copy Progress

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesCopied** | **Long** | Bytes copied during the copy of disk. |  [optional] [readonly] |
|**percentComplete** | **Integer** | Indicates the percentage completed for the copy of the disk. |  [optional] [readonly] |
|**serialNumber** | **String** | The serial number of the disk |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The Status of the copy |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| COMPLETED_WITH_ERRORS | &quot;CompletedWithErrors&quot; |
| FAILED | &quot;Failed&quot; |
| NOT_RETURNED | &quot;NotReturned&quot; |



