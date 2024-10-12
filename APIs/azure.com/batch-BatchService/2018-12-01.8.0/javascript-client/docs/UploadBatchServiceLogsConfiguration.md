# BatchService.UploadBatchServiceLogsConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerUrl** | **String** | The URL must include a Shared Access Signature (SAS) granting write permissions to the container. The SAS duration must allow enough time for the upload to finish. The start time for SAS is optional and recommended to not be specified. | 
**endTime** | **Date** | Any log file containing a log message in the time range will be uploaded. This means that the operation might retrieve more logs than have been requested since the entire log file is always uploaded, but the operation should not retrieve fewer logs than have been requested. If omitted, the default is to upload all logs available after the startTime. | [optional] 
**startTime** | **Date** | Any log file containing a log message in the time range will be uploaded. This means that the operation might retrieve more logs than have been requested since the entire log file is always uploaded, but the operation should not retrieve fewer logs than have been requested. | 


