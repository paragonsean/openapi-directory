

# AdminConversationsArchiveErrorSchema

Schema for error response from admin.conversations.archive

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| FEATURE_NOT_ENABLED | &quot;feature_not_enabled&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| CHANNEL_TYPE_NOT_SUPPORTED | &quot;channel_type_not_supported&quot; |
| DEFAULT_ORG_WIDE_CHANNEL | &quot;default_org_wide_channel&quot; |
| ALREADY_ARCHIVED | &quot;already_archived&quot; |
| CANT_ARCHIVE_GENERAL | &quot;cant_archive_general&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| COULD_NOT_ARCHIVE_CHANNEL | &quot;could_not_archive_channel&quot; |



