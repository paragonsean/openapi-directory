# FilesComApi.HistoryExportResultEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | What action was taken. Valid values: &#x60;create&#x60;, &#x60;read&#x60;, &#x60;update&#x60;, &#x60;destroy&#x60;, &#x60;move&#x60;, &#x60;login&#x60;, &#x60;failedlogin&#x60;, &#x60;copy&#x60;, &#x60;user_create&#x60;, &#x60;user_update&#x60;, &#x60;user_destroy&#x60;, &#x60;group_create&#x60;, &#x60;group_update&#x60;, &#x60;group_destroy&#x60;, &#x60;permission_create&#x60;, &#x60;permission_destroy&#x60;, &#x60;api_key_create&#x60;, &#x60;api_key_update&#x60;, &#x60;api_key_destroy&#x60; | [optional] 
**createdAt** | **Number** | When the action happened | [optional] 
**createdAtIso8601** | **Number** | When the action happened, in ISO8601 format. | [optional] 
**destination** | **String** | File moved to this destination folder | [optional] 
**failureType** | **String** | The type of login failure, if applicable.  Valid values: &#x60;expired_trial&#x60;, &#x60;account_overdue&#x60;, &#x60;locked_out&#x60;, &#x60;ip_mismatch&#x60;, &#x60;password_mismatch&#x60;, &#x60;site_mismatch&#x60;, &#x60;username_not_found&#x60;, &#x60;none&#x60;, &#x60;no_ftp_permission&#x60;, &#x60;no_web_permission&#x60;, &#x60;no_directory&#x60;, &#x60;errno_enoent&#x60;, &#x60;no_sftp_permission&#x60;, &#x60;no_dav_permission&#x60;, &#x60;no_restapi_permission&#x60;, &#x60;key_mismatch&#x60;, &#x60;region_mismatch&#x60;, &#x60;expired_access&#x60;, &#x60;desktop_ip_mismatch&#x60;, &#x60;desktop_api_key_not_used_quickly_enough&#x60;, &#x60;disabled&#x60;, &#x60;country_mismatch&#x60; | [optional] 
**fileId** | **Number** | File ID related to the action | [optional] 
**folder** | **String** | Folder in which the action occurred | [optional] 
**id** | **Number** | Action ID | [optional] 
**_interface** | **String** | Inteface through which the action was taken. Valid values: &#x60;web&#x60;, &#x60;ftp&#x60;, &#x60;robot&#x60;, &#x60;jsapi&#x60;, &#x60;webdesktopapi&#x60;, &#x60;sftp&#x60;, &#x60;dav&#x60;, &#x60;desktop&#x60;, &#x60;restapi&#x60;, &#x60;scim&#x60;, &#x60;office&#x60;, &#x60;mobile&#x60;, &#x60;as2&#x60;, &#x60;inbound_email&#x60;, &#x60;remote&#x60; | [optional] 
**ip** | **String** | Client IP that performed the action | [optional] 
**parentId** | **Number** | ID of the parent folder | [optional] 
**path** | **String** | Path of the related action | [optional] 
**src** | **String** | File move originated from this path | [optional] 
**targetExpiresAt** | **Number** | If searching for Histories about API keys, this is when the API key will expire | [optional] 
**targetId** | **Number** | ID of the object (such as Users, or API Keys) on which the action was taken | [optional] 
**targetName** | **String** | Name of the User, Group or other object with a name related to this action | [optional] 
**targetPermission** | **String** | Permission level of the action | [optional] 
**targetPermissionSet** | **String** | If searching for Histories about API keys, this represents the permission set of the associated  API key | [optional] 
**targetPlatform** | **String** | If searching for Histories about API keys, this is the platform on which the action was taken | [optional] 
**targetRecursive** | **Boolean** | Whether or not the action was recursive | [optional] 
**targetUserId** | **Number** | If searching for Histories about API keys, this is the User ID on which the action was taken | [optional] 
**targetUsername** | **String** | If searching for Histories about API keys, this is the username on which the action was taken | [optional] 
**userId** | **Number** | User ID | [optional] 
**username** | **String** | Username of the user that performed the action | [optional] 


