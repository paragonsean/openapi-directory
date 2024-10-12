

# ChatUpdateErrorSchema

Schema for error response chat.update method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| MESSAGE_NOT_FOUND | &quot;message_not_found&quot; |
| CANT_UPDATE_MESSAGE | &quot;cant_update_message&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| EDIT_WINDOW_CLOSED | &quot;edit_window_closed&quot; |
| MSG_TOO_LONG | &quot;msg_too_long&quot; |
| TOO_MANY_ATTACHMENTS | &quot;too_many_attachments&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| NO_TEXT | &quot;no_text&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| TOKEN_REVOKED | &quot;token_revoked&quot; |
| NO_PERMISSION | &quot;no_permission&quot; |
| INVALID_ARG_NAME | &quot;invalid_arg_name&quot; |
| INVALID_ARRAY_ARG | &quot;invalid_array_arg&quot; |
| INVALID_CHARSET | &quot;invalid_charset&quot; |
| INVALID_FORM_DATA | &quot;invalid_form_data&quot; |
| INVALID_POST_TYPE | &quot;invalid_post_type&quot; |
| MISSING_POST_TYPE | &quot;missing_post_type&quot; |
| REQUEST_TIMEOUT | &quot;request_timeout&quot; |
| INVALID_JSON | &quot;invalid_json&quot; |
| JSON_NOT_OBJECT | &quot;json_not_object&quot; |
| UPGRADE_REQUIRED | &quot;upgrade_required&quot; |
| FATAL_ERROR | &quot;fatal_error&quot; |
| IS_INACTIVE | &quot;is_inactive&quot; |



