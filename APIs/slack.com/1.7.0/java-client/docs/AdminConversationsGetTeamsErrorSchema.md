

# AdminConversationsGetTeamsErrorSchema

Schema for error response from admin.conversations.getTeams

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
| UNSUPPORTED_TEAM_TYPE | &quot;unsupported_team_type&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| COULD_NOT_GET_TEAMS | &quot;could_not_get_teams&quot; |
| INVALID_CURSOR | &quot;invalid_cursor&quot; |
| INVALID_LIMIT | &quot;invalid_limit&quot; |



