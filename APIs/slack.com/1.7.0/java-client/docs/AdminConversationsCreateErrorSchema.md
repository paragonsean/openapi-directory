

# AdminConversationsCreateErrorSchema

Schema for error response from admin.conversations.create

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| FEATURE_NOT_ENABLED | &quot;feature_not_enabled&quot; |
| NAME_TAKEN | &quot;name_taken&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| TEAM_NOT_FOUND | &quot;team_not_found&quot; |
| INVALID_TEAM | &quot;invalid_team&quot; |
| INVALID_NAME | &quot;invalid_name&quot; |
| COULD_NOT_CREATE_CHANNEL | &quot;could_not_create_channel&quot; |
| TEAM_ID_OR_ORG_REQUIRED | &quot;team_id_or_org_required&quot; |



