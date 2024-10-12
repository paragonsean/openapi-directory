# IotHubClient.JobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeUtc** | **String** | The time the job stopped processing. | [optional] [readonly] 
**failureReason** | **String** | If status &#x3D;&#x3D; failed, this string containing the reason for the failure. | [optional] [readonly] 
**jobId** | **String** | The job identifier. | [optional] [readonly] 
**parentJobId** | **String** | The job identifier of the parent job, if any. | [optional] [readonly] 
**startTimeUtc** | **String** | The start time of the job. | [optional] [readonly] 
**status** | **String** | The status of the job. | [optional] [readonly] 
**statusMessage** | **String** | The status message for the job. | [optional] [readonly] 
**type** | **String** | The type of the job. | [optional] [readonly] 



## Enum: StatusEnum


* `unknown` (value: `"unknown"`)

* `enqueued` (value: `"enqueued"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)

* `failed` (value: `"failed"`)

* `cancelled` (value: `"cancelled"`)





## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `export` (value: `"export"`)

* `import` (value: `"import"`)

* `backup` (value: `"backup"`)

* `readDeviceProperties` (value: `"readDeviceProperties"`)

* `writeDeviceProperties` (value: `"writeDeviceProperties"`)

* `updateDeviceConfiguration` (value: `"updateDeviceConfiguration"`)

* `rebootDevice` (value: `"rebootDevice"`)

* `factoryResetDevice` (value: `"factoryResetDevice"`)

* `firmwareUpdate` (value: `"firmwareUpdate"`)




