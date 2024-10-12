

# AdminConversationsSearchErrorSchema

Schema for error response from admin.conversations.search

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
| TEAM_NOT_FOUND | &quot;team_not_found&quot; |
| NOT_ALLOWED | &quot;not_allowed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| INVALID_CURSOR | &quot;invalid_cursor&quot; |
| INVALID_SEARCH_CHANNEL_TYPE | &quot;invalid_search_channel_type&quot; |
| INVALID_SORT | &quot;invalid_sort&quot; |
| INVALID_SORT_DIR | &quot;invalid_sort_dir&quot; |



