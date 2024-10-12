# ArtifactRegistryApi.ProjectSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacyRedirectionState** | **String** | The redirection state of the legacy repositories in this project. | [optional] 
**name** | **String** | The name of the project&#39;s settings. Always of the form: projects/{project-id}/projectSettings In update request: never set In response: always set | [optional] 



## Enum: LegacyRedirectionStateEnum


* `STATE_UNSPECIFIED` (value: `"REDIRECTION_STATE_UNSPECIFIED"`)

* `FROM_GCR_IO_DISABLED` (value: `"REDIRECTION_FROM_GCR_IO_DISABLED"`)

* `FROM_GCR_IO_ENABLED` (value: `"REDIRECTION_FROM_GCR_IO_ENABLED"`)

* `FROM_GCR_IO_FINALIZED` (value: `"REDIRECTION_FROM_GCR_IO_FINALIZED"`)




