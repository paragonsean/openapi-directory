

# StarsAddErrorSchema

Schema for error response from stars.add method

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callstack** | **String** | Note: PHP callstack is only visible in dev/qa |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**ok** | **Boolean** |  |  |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| BAD_TIMESTAMP | &quot;bad_timestamp&quot; |
| MESSAGE_NOT_FOUND | &quot;message_not_found&quot; |
| FILE_NOT_FOUND | &quot;file_not_found&quot; |
| FILE_COMMENT_NOT_FOUND | &quot;file_comment_not_found&quot; |
| CHANNEL_NOT_FOUND | &quot;channel_not_found&quot; |
| NO_ITEM_SPECIFIED | &quot;no_item_specified&quot; |
| ALREADY_STARRED | &quot;already_starred&quot; |
| NOT_AUTHED | &quot;not_authed&quot; |
| INVALID_AUTH | &quot;invalid_auth&quot; |
| ACCOUNT_INACTIVE | &quot;account_inactive&quot; |
| TOKEN_REVOKED | &quot;token_revoked&quot; |
| NO_PERMISSION | &quot;no_permission&quot; |
| ORG_LOGIN_REQUIRED | &quot;org_login_required&quot; |
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



