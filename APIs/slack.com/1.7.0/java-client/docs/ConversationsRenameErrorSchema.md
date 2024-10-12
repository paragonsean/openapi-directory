

# ConversationsRenameErrorSchema

Schema for error response from conversations.rename method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**needed** | **String** |  |  [optional] |
|**ok** | **Boolean** |  |  |
|**provided** | **String** |  |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| USER_IS_RESTRICTED | &quot;user_is_restricted&quot; |
| METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE | &quot;method_not_supported_for_channel_type&quot; |
| MISSING_SCOPE | &quot;missing_scope&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| NOT_IN_CHANNEL | &quot;not_in_channel&quot; |
| NOT_AUTHORIZED | &quot;not_authorized&quot; |
| INVALID_NAME | &quot;invalid_name&quot; |
| NAME_TAKEN | &quot;name_taken&quot; |
| INVALID_NAME_REQUIRED | &quot;invalid_name_required&quot; |
| INVALID_NAME_PUNCTUATION | &quot;invalid_name_punctuation&quot; |
| INVALID_NAME_MAXLENGTH | &quot;invalid_name_maxlength&quot; |
| INVALID_NAME_SPECIALS | &quot;invalid_name_specials&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| INVALID_ARG_NAME | &quot;invalid_arg_name&quot; |
| INVALID_ARRAY_ARG | &quot;invalid_array_arg&quot; |
| INVALID_CHARSET | &quot;invalid_charset&quot; |
| INVALID_FORM_DATA | &quot;invalid_form_data&quot; |
| INVALID_POST_TYPE | &quot;invalid_post_type&quot; |
| MISSING_POST_TYPE | &quot;missing_post_type&quot; |
| INVALID_JSON | &quot;invalid_json&quot; |
| JSON_NOT_OBJECT | &quot;json_not_object&quot; |
| REQUEST_TIMEOUT | &quot;request_timeout&quot; |
| UPGRADE_REQUIRED | &quot;upgrade_required&quot; |



