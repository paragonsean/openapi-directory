

# ConversationsOpenErrorSchema

Schema for error response from conversations.open method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE | &quot;method_not_supported_for_channel_type&quot; |
| USER_NOT_FOUND | &quot;user_not_found&quot; |
| USER_NOT_VISIBLE | &quot;user_not_visible&quot; |
| USER_DISABLED | &quot;user_disabled&quot; |
| USERS_LIST_NOT_SUPPLIED | &quot;users_list_not_supplied&quot; |
| NOT_ENOUGH_USERS | &quot;not_enough_users&quot; |
| TOO_MANY_USERS | &quot;too_many_users&quot; |
| INVALID_USER_COMBINATION | &quot;invalid_user_combination&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| INVALID_ARG_NAME | &quot;invalid_arg_name&quot; |
| INVALID_ARRAY_ARG | &quot;invalid_array_arg&quot; |
| INVALID_CHARSET | &quot;invalid_charset&quot; |
| INVALID_FORM_DATA | &quot;invalid_form_data&quot; |
| INVALID_POST_TYPE | &quot;invalid_post_type&quot; |
| MISSING_POST_TYPE | &quot;missing_post_type&quot; |
| TEAM_ADDED_TO_ORG | &quot;team_added_to_org&quot; |
| INVALID_JSON | &quot;invalid_json&quot; |
| JSON_NOT_OBJECT | &quot;json_not_object&quot; |
| REQUEST_TIMEOUT | &quot;request_timeout&quot; |
| UPGRADE_REQUIRED | &quot;upgrade_required&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |



