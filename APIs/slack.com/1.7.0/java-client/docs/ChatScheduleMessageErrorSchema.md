

# ChatScheduleMessageErrorSchema

Schema for error response chat.scheduleMessage method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| INVALID_TIME | &quot;invalid_time&quot; |
| TIME_IN_PAST | &quot;time_in_past&quot; |
| TIME_TOO_FAR | &quot;time_too_far&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| NOT_IN_CHANNEL | &quot;not_in_channel&quot; |
| IS_ARCHIVED | &quot;is_archived&quot; |
| MSG_TOO_LONG | &quot;msg_too_long&quot; |
| NO_TEXT | &quot;no_text&quot; |
| RESTRICTED_ACTION | &quot;restricted_action&quot; |
| RESTRICTED_ACTION_READ_ONLY_CHANNEL | &quot;restricted_action_read_only_channel&quot; |
| RESTRICTED_ACTION_THREAD_ONLY_CHANNEL | &quot;restricted_action_thread_only_channel&quot; |
| RESTRICTED_ACTION_NON_THREADABLE_CHANNEL | &quot;restricted_action_non_threadable_channel&quot; |
| TOO_MANY_ATTACHMENTS | &quot;too_many_attachments&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| TOKEN_REVOKED | &quot;token_revoked&quot; |
| NO_PERMISSION | &quot;no_permission&quot; |
| ORG_LOGIN_REQUIRED | &quot;org_login_required&quot; |
| EKM_ACCESS_DENIED | &quot;ekm_access_denied&quot; |
| MISSING_SCOPE | &quot;missing_scope&quot; |
| INVALID_ARGUMENTS | &quot;invalid_arguments&quot; |
| INVALID_ARG_NAME | &quot;invalid_arg_name&quot; |
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



