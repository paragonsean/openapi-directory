

# AdminConversationsUnarchiveErrorSchema

Schema for error response from admin.conversations.getConversationPrefs

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
| NOT_AN_ENTERPRISE | &quot;not_an_enterprise&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| MISSING_SCOPE | &quot;missing_scope&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| CHANNEL_TYPE_NOT_SUPPORTED | &quot;channel_type_not_supported&quot; |
| COULD_NOT_GET_CONVERSATION_PREFS | &quot;could_not_get_conversation_prefs&quot; |



