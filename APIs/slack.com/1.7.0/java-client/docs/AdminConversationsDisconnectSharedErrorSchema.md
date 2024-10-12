

# AdminConversationsDisconnectSharedErrorSchema

Schema for error response from admin.conversations.disconnectShared

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
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| NOT_SUPPORTED | &quot;not_supported&quot; |
| TEAM_NOT_FOUND | &quot;team_not_found&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| MISSING_SCOPE | &quot;missing_scope&quot; |
| LEAVING_TEAM_NOT_IN_CHANNEL | &quot;leaving_team_not_in_channel&quot; |
| NO_TEAMS_TO_DISCONNECT | &quot;no_teams_to_disconnect&quot; |
| LEAVING_TEAM_REQUIRED | &quot;leaving_team_required&quot; |
| CANNOT_KICK_TEAM | &quot;cannot_kick_team&quot; |
| CANNOT_KICK_HOME_TEAM | &quot;cannot_kick_home_team&quot; |



