# FilesComApi.ApiKeyEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Time which API Key was created | [optional] 
**description** | **String** | User-supplied description of API key. | [optional] 
**descriptiveLabel** | **String** | Unique label that describes this API key.  Useful for external systems where you may have API keys from multiple accounts and want a human-readable label for each key. | [optional] 
**expiresAt** | **Date** | API Key expiration date | [optional] 
**id** | **Number** | API Key ID | [optional] 
**key** | **String** | API Key actual key string | [optional] 
**lastUseAt** | **Date** | API Key last used - note this value is only updated once per 3 hour period, so the &#39;actual&#39; time of last use may be up to 3 hours later than this timestamp. | [optional] 
**name** | **String** | Internal name for the API Key.  For your use. | [optional] 
**path** | **String** | Folder path restriction for this api key. | [optional] 
**permissionSet** | **String** | Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] 
**platform** | **String** | If this API key represents a Desktop app, what platform was it created on? | [optional] 
**url** | **String** | URL for API host. | [optional] 
**userId** | **Number** | User ID for the owner of this API Key.  May be blank for Site-wide API Keys. | [optional] 



## Enum: PermissionSetEnum


* `none` (value: `"none"`)

* `full` (value: `"full"`)

* `desktop_app` (value: `"desktop_app"`)

* `sync_app` (value: `"sync_app"`)

* `office_integration` (value: `"office_integration"`)

* `mobile_app` (value: `"mobile_app"`)




