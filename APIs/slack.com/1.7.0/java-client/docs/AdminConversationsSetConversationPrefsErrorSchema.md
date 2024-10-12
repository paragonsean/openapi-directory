

# AdminConversationsSetConversationPrefsErrorSchema

Schema for error response from admin.conversations.setConversationPrefs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| FEATURE_NOT_ENABLED | &quot;feature_not_enabled&quot; |
| NOT_AN_ADMIN | &quot;not_an_admin&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| CHANNEL_TYPE_NOT_SUPPORTED | &quot;channel_type_not_supported&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| MISSING_SCOPE | &quot;missing_scope&quot; |
| COULD_NOT_SET_CHANNEL_PREF | &quot;could_not_set_channel_pref&quot; |
| DEFAULT_ORG_WIDE_CHANNEL | &quot;default_org_wide_channel&quot; |



