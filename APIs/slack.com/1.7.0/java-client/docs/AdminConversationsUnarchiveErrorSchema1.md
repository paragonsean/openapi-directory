

# AdminConversationsUnarchiveErrorSchema1

Schema for error response from admin.conversations.rename

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
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| COULD_NOT_RENAME_CHANNEL | &quot;could_not_rename_channel&quot; |
| DEFAULT_ORG_WIDE_CHANNEL | &quot;default_org_wide_channel&quot; |
| NAME_TAKEN | &quot;name_taken&quot; |



