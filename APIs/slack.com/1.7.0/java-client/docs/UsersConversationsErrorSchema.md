

# UsersConversationsErrorSchema

Schema for error response from users.conversations method

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
| MISSING_SCOPE | &quot;missing_scope&quot; |
| INVALID_TYPES | &quot;invalid_types&quot; |
| INVALID_CURSOR | &quot;invalid_cursor&quot; |
| INVALID_LIMIT | &quot;invalid_limit&quot; |
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
| TEAM_ADDED_TO_ORG | &quot;team_added_to_org&quot; |
| INVALID_JSON | &quot;invalid_json&quot; |
| JSON_NOT_OBJECT | &quot;json_not_object&quot; |
| REQUEST_TIMEOUT | &quot;request_timeout&quot; |
| UPGRADE_REQUIRED | &quot;upgrade_required&quot; |
| FATAL_ERROR | &quot;fatal_error&quot; |



