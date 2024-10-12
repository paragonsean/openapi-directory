

# ChatPostMessageErrorSchema

Schema for error response chat.postMessage method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| NOT_IN_CHANNEL | &quot;not_in_channel&quot; |
| IS_ARCHIVED | &quot;is_archived&quot; |
| MSG_TOO_LONG | &quot;msg_too_long&quot; |
| NO_TEXT | &quot;no_text&quot; |
| TOO_MANY_ATTACHMENTS | &quot;too_many_attachments&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| INVALID_ARG_NAME | &quot;invalid_arg_name&quot; |
| INVALID_ARRAY_ARG | &quot;invalid_array_arg&quot; |
| INVALID_CHARSET | &quot;invalid_charset&quot; |
| INVALID_FORM_DATA | &quot;invalid_form_data&quot; |
| INVALID_POST_TYPE | &quot;invalid_post_type&quot; |
| MISSING_POST_TYPE | &quot;missing_post_type&quot; |



