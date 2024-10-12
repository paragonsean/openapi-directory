

# ActionEntity

List site full action history.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Type of action |  [optional] |
|**destination** | **String** | The destination path for this action, if applicable |  [optional] |
|**display** | **String** | Friendly displayed output |  [optional] |
|**failureType** | [**FailureTypeEnum**](#FailureTypeEnum) | Failure type.  If action was a user login or session failure, why did it fail? |  [optional] |
|**id** | **Integer** | Action ID |  [optional] |
|**_interface** | [**InterfaceEnum**](#InterfaceEnum) | Interface on which this action occurred. |  [optional] |
|**ip** | **String** | IP Address that performed this action |  [optional] |
|**path** | **String** | Path |  [optional] |
|**source** | **String** | The source path for this action, if applicable |  [optional] |
|**targets** | **List&lt;Object&gt;** | Targets |  [optional] |
|**userId** | **Integer** | User ID |  [optional] |
|**username** | **String** | Username |  [optional] |
|**when** | **OffsetDateTime** | Action occurrence date/time |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| CREATE | &quot;create&quot; |
| READ | &quot;read&quot; |
| UPDATE | &quot;update&quot; |
| DESTROY | &quot;destroy&quot; |
| MOVE | &quot;move&quot; |
| LOGIN | &quot;login&quot; |
| FAILEDLOGIN | &quot;failedlogin&quot; |
| COPY | &quot;copy&quot; |
| USER_CREATE | &quot;user_create&quot; |
| USER_UPDATE | &quot;user_update&quot; |
| USER_DESTROY | &quot;user_destroy&quot; |
| GROUP_CREATE | &quot;group_create&quot; |
| GROUP_UPDATE | &quot;group_update&quot; |
| GROUP_DESTROY | &quot;group_destroy&quot; |
| PERMISSION_CREATE | &quot;permission_create&quot; |
| PERMISSION_DESTROY | &quot;permission_destroy&quot; |
| API_KEY_CREATE | &quot;api_key_create&quot; |
| API_KEY_UPDATE | &quot;api_key_update&quot; |
| API_KEY_DESTROY | &quot;api_key_destroy&quot; |



## Enum: FailureTypeEnum

| Name | Value |
|---- | -----|
| EXPIRED_TRIAL | &quot;expired_trial&quot; |
| ACCOUNT_OVERDUE | &quot;account_overdue&quot; |
| LOCKED_OUT | &quot;locked_out&quot; |
| IP_MISMATCH | &quot;ip_mismatch&quot; |
| PASSWORD_MISMATCH | &quot;password_mismatch&quot; |
| SITE_MISMATCH | &quot;site_mismatch&quot; |
| USERNAME_NOT_FOUND | &quot;username_not_found&quot; |
| NONE | &quot;none&quot; |
| NO_FTP_PERMISSION | &quot;no_ftp_permission&quot; |
| NO_WEB_PERMISSION | &quot;no_web_permission&quot; |
| NO_DIRECTORY | &quot;no_directory&quot; |
| ERRNO_ENOENT | &quot;errno_enoent&quot; |
| NO_SFTP_PERMISSION | &quot;no_sftp_permission&quot; |
| NO_DAV_PERMISSION | &quot;no_dav_permission&quot; |
| NO_RESTAPI_PERMISSION | &quot;no_restapi_permission&quot; |
| KEY_MISMATCH | &quot;key_mismatch&quot; |
| REGION_MISMATCH | &quot;region_mismatch&quot; |
| EXPIRED_ACCESS | &quot;expired_access&quot; |
| DESKTOP_IP_MISMATCH | &quot;desktop_ip_mismatch&quot; |
| DESKTOP_API_KEY_NOT_USED_QUICKLY_ENOUGH | &quot;desktop_api_key_not_used_quickly_enough&quot; |
| DISABLED | &quot;disabled&quot; |
| COUNTRY_MISMATCH | &quot;country_mismatch&quot; |



## Enum: InterfaceEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| FTP | &quot;ftp&quot; |
| ROBOT | &quot;robot&quot; |
| JSAPI | &quot;jsapi&quot; |
| WEBDESKTOPAPI | &quot;webdesktopapi&quot; |
| SFTP | &quot;sftp&quot; |
| DAV | &quot;dav&quot; |
| DESKTOP | &quot;desktop&quot; |
| RESTAPI | &quot;restapi&quot; |
| SCIM | &quot;scim&quot; |
| OFFICE | &quot;office&quot; |
| MOBILE | &quot;mobile&quot; |
| AS2 | &quot;as2&quot; |
| INBOUND_EMAIL | &quot;inbound_email&quot; |
| REMOTE | &quot;remote&quot; |



