

# RemindersAddErrorSchema

Schema for error response from reminders.add method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| CANNOT_PARSE | &quot;cannot_parse&quot; |
| USER_NOT_FOUND | &quot;user_not_found&quot; |
| CANNOT_ADD_BOT | &quot;cannot_add_bot&quot; |
| CANNOT_ADD_SLACKBOT | &quot;cannot_add_slackbot&quot; |
| CANNOT_ADD_OTHERS | &quot;cannot_add_others&quot; |
| CANNOT_ADD_OTHERS_RECURRING | &quot;cannot_add_others_recurring&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| TOKEN_REVOKED | &quot;token_revoked&quot; |
| NO_PERMISSION | &quot;no_permission&quot; |
| ORG_LOGIN_REQUIRED | &quot;org_login_required&quot; |
| USER_IS_BOT | &quot;user_is_bot&quot; |
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
| FATAL_ERROR | &quot;fatal_error&quot; |



