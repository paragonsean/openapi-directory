# SlackWebApi.ConversationsMarkErrorSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callstack** | **String** | Note: PHP callstack is only visible in dev/qa | [optional] 
**error** | **String** |  | 
**needed** | **String** |  | [optional] 
**ok** | **Boolean** |  | 
**provided** | **String** |  | [optional] 



## Enum: ErrorEnum


* `method_not_supported_for_channel_type` (value: `"method_not_supported_for_channel_type"`)

* `missing_scope` (value: `"missing_scope"`)

* `channel_not_found` (value: `"channel_not_found"`)

* `invalid_timestamp` (value: `"invalid_timestamp"`)

* `not_in_channel` (value: `"not_in_channel"`)

* `not_authed` (value: `"not_authed"`)

* `invalid_auth` (value: `"invalid_auth"`)

* `account_inactive` (value: `"account_inactive"`)

* `invalid_arg_name` (value: `"invalid_arg_name"`)

* `invalid_array_arg` (value: `"invalid_array_arg"`)

* `invalid_charset` (value: `"invalid_charset"`)

* `invalid_form_data` (value: `"invalid_form_data"`)

* `invalid_post_type` (value: `"invalid_post_type"`)

* `missing_post_type` (value: `"missing_post_type"`)

* `invalid_json` (value: `"invalid_json"`)

* `json_not_object` (value: `"json_not_object"`)

* `request_timeout` (value: `"request_timeout"`)

* `upgrade_required` (value: `"upgrade_required"`)

* `not_allowed_token_type` (value: `"not_allowed_token_type"`)




