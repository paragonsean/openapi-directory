

# CreateJobTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accelerationSettings** | [**CreateJobRequestAccelerationSettings**](CreateJobRequestAccelerationSettings.md) |  |  [optional] |
|**category** | **String** | Optional. A category for the job template you are creating |  [optional] |
|**description** | **String** | Optional. A description of the job template you are creating. |  [optional] |
|**hopDestinations** | [**List&lt;HopDestination&gt;**](HopDestination.md) | Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide. |  [optional] |
|**name** | **String** | The name of the job template you are creating. |  |
|**priority** | **Integer** | Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don&#39;t specify a priority, the service uses the default value 0. |  [optional] |
|**queue** | **String** | Optional. The queue that jobs created from this template are assigned to. If you don&#39;t specify this, jobs will go to the default queue. |  [optional] |
|**settings** | [**CreateJobTemplateRequestSettings**](CreateJobTemplateRequestSettings.md) |  |  |
|**statusUpdateInterval** | [**StatusUpdateIntervalEnum**](#StatusUpdateIntervalEnum) | Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. |  [optional] |



## Enum: StatusUpdateIntervalEnum

| Name | Value |
|---- | -----|
| _10 | &quot;SECONDS_10&quot; |
| _12 | &quot;SECONDS_12&quot; |
| _15 | &quot;SECONDS_15&quot; |
| _20 | &quot;SECONDS_20&quot; |
| _30 | &quot;SECONDS_30&quot; |
| _60 | &quot;SECONDS_60&quot; |
| _120 | &quot;SECONDS_120&quot; |
| _180 | &quot;SECONDS_180&quot; |
| _240 | &quot;SECONDS_240&quot; |
| _300 | &quot;SECONDS_300&quot; |
| _360 | &quot;SECONDS_360&quot; |
| _420 | &quot;SECONDS_420&quot; |
| _480 | &quot;SECONDS_480&quot; |
| _540 | &quot;SECONDS_540&quot; |
| _600 | &quot;SECONDS_600&quot; |



