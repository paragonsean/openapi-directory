

# CreateJobForDevicesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceIds** | **List&lt;String&gt;** | ID of target device. |  |
|**deviceJobConfig** | [**CreateJobForDevicesRequestDeviceJobConfig**](CreateJobForDevicesRequestDeviceJobConfig.md) |  |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | The type of job to run. |  |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| OTA | &quot;OTA&quot; |
| REBOOT | &quot;REBOOT&quot; |



