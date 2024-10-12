

# LogsPolicy

LogsPolicy describes how outputs from a Job's Tasks (stdout/stderr) will be preserved.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudLoggingOption** | [**CloudLoggingOption**](CloudLoggingOption.md) |  |  [optional] |
|**destination** | [**DestinationEnum**](#DestinationEnum) | Where logs should be saved. |  [optional] |
|**logsPath** | **String** | The path to which logs are saved when the destination &#x3D; PATH. This can be a local file path on the VM, or under the mount point of a Persistent Disk or Filestore, or a Cloud Storage path. |  [optional] |



## Enum: DestinationEnum

| Name | Value |
|---- | -----|
| DESTINATION_UNSPECIFIED | &quot;DESTINATION_UNSPECIFIED&quot; |
| CLOUD_LOGGING | &quot;CLOUD_LOGGING&quot; |
| PATH | &quot;PATH&quot; |



