# AwsElementalMediaConvert.CreateJobTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerationSettings** | [**CreateJobRequestAccelerationSettings**](CreateJobRequestAccelerationSettings.md) |  | [optional] 
**category** | **String** | Optional. A category for the job template you are creating | [optional] 
**description** | **String** | Optional. A description of the job template you are creating. | [optional] 
**hopDestinations** | [**[HopDestination]**](HopDestination.md) | Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide. | [optional] 
**name** | **String** | The name of the job template you are creating. | 
**priority** | **Number** | Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don&#39;t specify a priority, the service uses the default value 0. | [optional] 
**queue** | **String** | Optional. The queue that jobs created from this template are assigned to. If you don&#39;t specify this, jobs will go to the default queue. | [optional] 
**settings** | [**CreateJobTemplateRequestSettings**](CreateJobTemplateRequestSettings.md) |  | 
**statusUpdateInterval** | **String** | Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. | [optional] 
**tags** | **{String: String}** | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. | [optional] 



## Enum: StatusUpdateIntervalEnum


* `10` (value: `"SECONDS_10"`)

* `12` (value: `"SECONDS_12"`)

* `15` (value: `"SECONDS_15"`)

* `20` (value: `"SECONDS_20"`)

* `30` (value: `"SECONDS_30"`)

* `60` (value: `"SECONDS_60"`)

* `120` (value: `"SECONDS_120"`)

* `180` (value: `"SECONDS_180"`)

* `240` (value: `"SECONDS_240"`)

* `300` (value: `"SECONDS_300"`)

* `360` (value: `"SECONDS_360"`)

* `420` (value: `"SECONDS_420"`)

* `480` (value: `"SECONDS_480"`)

* `540` (value: `"SECONDS_540"`)

* `600` (value: `"SECONDS_600"`)




