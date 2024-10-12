

# HistoryExportEntity

Show History Export

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endAt** | **OffsetDateTime** | End date/time of export range. |  [optional] |
|**historyVersion** | **String** | Version of the history for the export. |  [optional] |
|**id** | **Integer** | History Export ID |  [optional] |
|**queryAction** | **String** | Filter results by this this action type. Valid values: &#x60;create&#x60;, &#x60;read&#x60;, &#x60;update&#x60;, &#x60;destroy&#x60;, &#x60;move&#x60;, &#x60;login&#x60;, &#x60;failedlogin&#x60;, &#x60;copy&#x60;, &#x60;user_create&#x60;, &#x60;user_update&#x60;, &#x60;user_destroy&#x60;, &#x60;group_create&#x60;, &#x60;group_update&#x60;, &#x60;group_destroy&#x60;, &#x60;permission_create&#x60;, &#x60;permission_destroy&#x60;, &#x60;api_key_create&#x60;, &#x60;api_key_update&#x60;, &#x60;api_key_destroy&#x60; |  [optional] |
|**queryDestination** | **String** | Return results that are file moves with this path as destination. |  [optional] |
|**queryFailureType** | **String** | If searching for Histories about login failures, this parameter restricts results to failures of this specific type.  Valid values: &#x60;expired_trial&#x60;, &#x60;account_overdue&#x60;, &#x60;locked_out&#x60;, &#x60;ip_mismatch&#x60;, &#x60;password_mismatch&#x60;, &#x60;site_mismatch&#x60;, &#x60;username_not_found&#x60;, &#x60;none&#x60;, &#x60;no_ftp_permission&#x60;, &#x60;no_web_permission&#x60;, &#x60;no_directory&#x60;, &#x60;errno_enoent&#x60;, &#x60;no_sftp_permission&#x60;, &#x60;no_dav_permission&#x60;, &#x60;no_restapi_permission&#x60;, &#x60;key_mismatch&#x60;, &#x60;region_mismatch&#x60;, &#x60;expired_access&#x60;, &#x60;desktop_ip_mismatch&#x60;, &#x60;desktop_api_key_not_used_quickly_enough&#x60;, &#x60;disabled&#x60;, &#x60;country_mismatch&#x60; |  [optional] |
|**queryFileId** | **String** | Return results that are file actions related to the file indicated by this File ID |  [optional] |
|**queryFolder** | **String** | Return results that are file actions related to files or folders inside this folder path. |  [optional] |
|**queryInterface** | **String** | Filter results by this this interface type. Valid values: &#x60;web&#x60;, &#x60;ftp&#x60;, &#x60;robot&#x60;, &#x60;jsapi&#x60;, &#x60;webdesktopapi&#x60;, &#x60;sftp&#x60;, &#x60;dav&#x60;, &#x60;desktop&#x60;, &#x60;restapi&#x60;, &#x60;scim&#x60;, &#x60;office&#x60;, &#x60;mobile&#x60;, &#x60;as2&#x60;, &#x60;inbound_email&#x60;, &#x60;remote&#x60; |  [optional] |
|**queryIp** | **String** | Filter results by this IP address. |  [optional] |
|**queryParentId** | **String** | Return results that are file actions inside the parent folder specified by this folder ID |  [optional] |
|**queryPath** | **String** | Return results that are file actions related to this path. |  [optional] |
|**querySrc** | **String** | Return results that are file moves originating from this path. |  [optional] |
|**queryTargetId** | **String** | If searching for Histories about specific objects (such as Users, or API Keys), this paremeter restricts results to objects that match this ID. |  [optional] |
|**queryTargetName** | **String** | If searching for Histories about Users, Groups or other objects with names, this parameter restricts results to objects with this name/username. |  [optional] |
|**queryTargetPermission** | **String** | If searching for Histories about Permisisons, this parameter restricts results to permissions of this level. |  [optional] |
|**queryTargetPermissionSet** | **String** | If searching for Histories about API keys, this parameter restricts results to API keys with this permission set. |  [optional] |
|**queryTargetPlatform** | **String** | If searching for Histories about API keys, this parameter restricts results to API keys associated with this platform. |  [optional] |
|**queryTargetUserId** | **String** | If searching for Histories about API keys, this parameter restricts results to API keys created by/for this user ID. |  [optional] |
|**queryTargetUsername** | **String** | If searching for Histories about API keys, this parameter restricts results to API keys created by/for this username. |  [optional] |
|**queryUserId** | **String** | Return results that are actions performed by the user indiciated by this User ID |  [optional] |
|**queryUsername** | **String** | Filter results by this username. |  [optional] |
|**resultsUrl** | **String** | If &#x60;status&#x60; is &#x60;ready&#x60;, this will be a URL where all the results can be downloaded at once as a CSV. |  [optional] |
|**startAt** | **OffsetDateTime** | Start date/time of export range. |  [optional] |
|**status** | **String** | Status of export.  Will be: &#x60;building&#x60;, &#x60;ready&#x60;, or &#x60;failed&#x60; |  [optional] |



