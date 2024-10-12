

# AdminConversationsConvertToPrivateErrorSchema

Schema for error response from admin.conversations.convertToPrivate

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| FEATURE_NOT_ENABLED | &quot;feature_not_enabled&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| NAME_TAKEN | &quot;name_taken&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| CHANNEL_TYPE_NOT_SUPPORTED | &quot;channel_type_not_supported&quot; |
| DEFAULT_ORG_WIDE_CHANNEL | &quot;default_org_wide_channel&quot; |
| METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE | &quot;method_not_supported_for_channel_type&quot; |
| COULD_NOT_CONVERT_CHANNEL | &quot;could_not_convert_channel&quot; |
| EXTERNAL_CHANNEL_MIGRATING | &quot;external_channel_migrating&quot; |



