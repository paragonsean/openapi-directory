# BatchApi.LogsPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudLoggingOption** | [**CloudLoggingOption**](CloudLoggingOption.md) |  | [optional] 
**destination** | **String** | Where logs should be saved. | [optional] 
**logsPath** | **String** | The path to which logs are saved when the destination &#x3D; PATH. This can be a local file path on the VM, or under the mount point of a Persistent Disk or Filestore, or a Cloud Storage path. | [optional] 



## Enum: DestinationEnum


* `DESTINATION_UNSPECIFIED` (value: `"DESTINATION_UNSPECIFIED"`)

* `CLOUD_LOGGING` (value: `"CLOUD_LOGGING"`)

* `PATH` (value: `"PATH"`)




