

# JobResponse

The properties of the Job Response object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeUtc** | **String** | The time the job stopped processing. |  [optional] [readonly] |
|**failureReason** | **String** | If status &#x3D;&#x3D; failed, this string containing the reason for the failure. |  [optional] [readonly] |
|**jobId** | **String** | The job identifier. |  [optional] [readonly] |
|**parentJobId** | **String** | The job identifier of the parent job, if any. |  [optional] [readonly] |
|**startTimeUtc** | **String** | The start time of the job. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the job. |  [optional] [readonly] |
|**statusMessage** | **String** | The status message for the job. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the job. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| ENQUEUED | &quot;enqueued&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| EXPORT | &quot;export&quot; |
| IMPORT | &quot;import&quot; |
| BACKUP | &quot;backup&quot; |
| READ_DEVICE_PROPERTIES | &quot;readDeviceProperties&quot; |
| WRITE_DEVICE_PROPERTIES | &quot;writeDeviceProperties&quot; |
| UPDATE_DEVICE_CONFIGURATION | &quot;updateDeviceConfiguration&quot; |
| REBOOT_DEVICE | &quot;rebootDevice&quot; |
| FACTORY_RESET_DEVICE | &quot;factoryResetDevice&quot; |
| FIRMWARE_UPDATE | &quot;firmwareUpdate&quot; |



