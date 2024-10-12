

# CreateJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accelerationSettings** | [**CreateJobRequestAccelerationSettings**](CreateJobRequestAccelerationSettings.md) |  |  [optional] |
|**billingTagsSource** | [**BillingTagsSourceEnum**](#BillingTagsSourceEnum) | The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up. |  [optional] |
|**clientRequestToken** | **String** | Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html. |  [optional] |
|**hopDestinations** | [**List&lt;HopDestination&gt;**](HopDestination.md) | Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide. |  [optional] |
|**jobTemplate** | **String** | Optional. When you create a job, you can either specify a job template or specify the transcoding settings individually. |  [optional] |
|**priority** | **Integer** | Optional. Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don&#39;t specify a priority, the service uses the default value 0. |  [optional] |
|**queue** | **String** | Optional. When you create a job, you can specify a queue to send it to. If you don&#39;t specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html. |  [optional] |
|**role** | **String** | Required. The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html. |  |
|**settings** | [**CreateJobRequestSettings**](CreateJobRequestSettings.md) |  |  |
|**simulateReservedQueue** | [**SimulateReservedQueueEnum**](#SimulateReservedQueueEnum) | Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default. |  [optional] |
|**statusUpdateInterval** | [**StatusUpdateIntervalEnum**](#StatusUpdateIntervalEnum) | Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Optional. The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.  Use standard AWS tags on your job for automatic integration with AWS services and for custom integrations and workflows. |  [optional] |
|**userMetadata** | **Map&lt;String, String&gt;** | Optional. User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs.  Use only for existing integrations or workflows that rely on job metadata tags. Otherwise, we recommend that you use standard AWS tags. |  [optional] |



## Enum: BillingTagsSourceEnum

| Name | Value |
|---- | -----|
| QUEUE | &quot;QUEUE&quot; |
| PRESET | &quot;PRESET&quot; |
| JOB_TEMPLATE | &quot;JOB_TEMPLATE&quot; |
| JOB | &quot;JOB&quot; |



## Enum: SimulateReservedQueueEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



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



