

# ProjectSettings

The Artifact Registry settings that apply to a Project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**legacyRedirectionState** | [**LegacyRedirectionStateEnum**](#LegacyRedirectionStateEnum) | The redirection state of the legacy repositories in this project. |  [optional] |
|**name** | **String** | The name of the project&#39;s settings. Always of the form: projects/{project-id}/projectSettings In update request: never set In response: always set |  [optional] |



## Enum: LegacyRedirectionStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;REDIRECTION_STATE_UNSPECIFIED&quot; |
| FROM_GCR_IO_DISABLED | &quot;REDIRECTION_FROM_GCR_IO_DISABLED&quot; |
| FROM_GCR_IO_ENABLED | &quot;REDIRECTION_FROM_GCR_IO_ENABLED&quot; |
| FROM_GCR_IO_FINALIZED | &quot;REDIRECTION_FROM_GCR_IO_FINALIZED&quot; |



