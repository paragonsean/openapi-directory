# DataPortabilityApi.PortabilityArchiveState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The resource name of ArchiveJob&#39;s PortabilityArchiveState singleton. The format is: archiveJobs/{archive_job}/portabilityArchiveState. archive_job is the job ID provided in the request. | [optional] 
**state** | **String** | Resource that represents the state of the Archive job. | [optional] 
**urls** | **[String]** | If the state is complete, this method returns the signed URLs of the objects in the Cloud Storage bucket. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




