

# AdminConversationsInviteErrorSchema

Schema for error response from admin.conversations.invite

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
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| USER_MUST_BE_ADMIN | &quot;user_must_be_admin&quot; |
| FAILED_FOR_SOME_USERS | &quot;failed_for_some_users&quot; |



