# FilesComApi.ActionEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Type of action | [optional] 
**destination** | **String** | The destination path for this action, if applicable | [optional] 
**display** | **String** | Friendly displayed output | [optional] 
**failureType** | **String** | Failure type.  If action was a user login or session failure, why did it fail? | [optional] 
**id** | **Number** | Action ID | [optional] 
**_interface** | **String** | Interface on which this action occurred. | [optional] 
**ip** | **String** | IP Address that performed this action | [optional] 
**path** | **String** | Path | [optional] 
**source** | **String** | The source path for this action, if applicable | [optional] 
**targets** | **[Object]** | Targets | [optional] 
**userId** | **Number** | User ID | [optional] 
**username** | **String** | Username | [optional] 
**when** | **Date** | Action occurrence date/time | [optional] 



## Enum: ActionEnum


* `create` (value: `"create"`)

* `read` (value: `"read"`)

* `update` (value: `"update"`)

* `destroy` (value: `"destroy"`)

* `move` (value: `"move"`)

* `login` (value: `"login"`)

* `failedlogin` (value: `"failedlogin"`)

* `copy` (value: `"copy"`)

* `user_create` (value: `"user_create"`)

* `user_update` (value: `"user_update"`)

* `user_destroy` (value: `"user_destroy"`)

* `group_create` (value: `"group_create"`)

* `group_update` (value: `"group_update"`)

* `group_destroy` (value: `"group_destroy"`)

* `permission_create` (value: `"permission_create"`)

* `permission_destroy` (value: `"permission_destroy"`)

* `api_key_create` (value: `"api_key_create"`)

* `api_key_update` (value: `"api_key_update"`)

* `api_key_destroy` (value: `"api_key_destroy"`)





## Enum: FailureTypeEnum


* `expired_trial` (value: `"expired_trial"`)

* `account_overdue` (value: `"account_overdue"`)

* `locked_out` (value: `"locked_out"`)

* `ip_mismatch` (value: `"ip_mismatch"`)

* `password_mismatch` (value: `"password_mismatch"`)

* `site_mismatch` (value: `"site_mismatch"`)

* `username_not_found` (value: `"username_not_found"`)

* `none` (value: `"none"`)

* `no_ftp_permission` (value: `"no_ftp_permission"`)

* `no_web_permission` (value: `"no_web_permission"`)

* `no_directory` (value: `"no_directory"`)

* `errno_enoent` (value: `"errno_enoent"`)

* `no_sftp_permission` (value: `"no_sftp_permission"`)

* `no_dav_permission` (value: `"no_dav_permission"`)

* `no_restapi_permission` (value: `"no_restapi_permission"`)

* `key_mismatch` (value: `"key_mismatch"`)

* `region_mismatch` (value: `"region_mismatch"`)

* `expired_access` (value: `"expired_access"`)

* `desktop_ip_mismatch` (value: `"desktop_ip_mismatch"`)

* `desktop_api_key_not_used_quickly_enough` (value: `"desktop_api_key_not_used_quickly_enough"`)

* `disabled` (value: `"disabled"`)

* `country_mismatch` (value: `"country_mismatch"`)





## Enum: InterfaceEnum


* `web` (value: `"web"`)

* `ftp` (value: `"ftp"`)

* `robot` (value: `"robot"`)

* `jsapi` (value: `"jsapi"`)

* `webdesktopapi` (value: `"webdesktopapi"`)

* `sftp` (value: `"sftp"`)

* `dav` (value: `"dav"`)

* `desktop` (value: `"desktop"`)

* `restapi` (value: `"restapi"`)

* `scim` (value: `"scim"`)

* `office` (value: `"office"`)

* `mobile` (value: `"mobile"`)

* `as2` (value: `"as2"`)

* `inbound_email` (value: `"inbound_email"`)

* `remote` (value: `"remote"`)




