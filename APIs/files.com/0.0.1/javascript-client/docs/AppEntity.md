# FilesComApi.AppEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appType** | **String** | The type of the App | [optional] 
**documentationLinks** | **Object** | Collection of named links to documentation | [optional] 
**extendedDescription** | **String** | Long form description of the App | [optional] 
**externalHomepageUrl** | **String** | Link to external homepage | [optional] 
**featured** | **Boolean** | Is featured on the App listing? | [optional] 
**folderBehaviorType** | **String** | Associated Folder Behavior type, if any | [optional] 
**iconUrl** | **String** | App icon | [optional] 
**logoThumbnailUrl** | **String** | Logo thumbnail for the App | [optional] 
**logoUrl** | **String** | Full size logo for the App | [optional] 
**marketingYoutubeUrl** | **String** | Marketing video page | [optional] 
**name** | **String** | Name of the App | [optional] 
**remoteServerType** | **String** | Associated Remote Server type, if any | [optional] 
**screenshotListUrls** | **[String]** | Screenshots of the App | [optional] 
**shortDescription** | **String** | Short description of the App | [optional] 
**ssoStrategyType** | **String** | Associated SSO Strategy type, if any | [optional] 
**tutorialYoutubeUrl** | **String** | Tutorial video page | [optional] 



## Enum: AppTypeEnum


* `sdk` (value: `"sdk"`)

* `sso` (value: `"sso"`)

* `remote_server` (value: `"remote_server"`)

* `folder_behavior` (value: `"folder_behavior"`)

* `client_app` (value: `"client_app"`)

* `app_integration` (value: `"app_integration"`)





## Enum: FolderBehaviorTypeEnum


* `webhook` (value: `"webhook"`)

* `file_expiration` (value: `"file_expiration"`)

* `auto_encrypt` (value: `"auto_encrypt"`)

* `lock_subfolders` (value: `"lock_subfolders"`)

* `storage_region` (value: `"storage_region"`)

* `serve_publicly` (value: `"serve_publicly"`)

* `create_user_folders` (value: `"create_user_folders"`)

* `remote_server_sync` (value: `"remote_server_sync"`)

* `inbox` (value: `"inbox"`)

* `append_timestamp` (value: `"append_timestamp"`)

* `limit_file_extensions` (value: `"limit_file_extensions"`)

* `limit_file_regex` (value: `"limit_file_regex"`)

* `amazon_sns` (value: `"amazon_sns"`)

* `watermark` (value: `"watermark"`)

* `remote_server_mount` (value: `"remote_server_mount"`)

* `slack_webhook` (value: `"slack_webhook"`)

* `auto_decrypt` (value: `"auto_decrypt"`)

* `override_upload_filename` (value: `"override_upload_filename"`)





## Enum: RemoteServerTypeEnum


* `ftp` (value: `"ftp"`)

* `sftp` (value: `"sftp"`)

* `s3` (value: `"s3"`)

* `google_cloud_storage` (value: `"google_cloud_storage"`)

* `webdav` (value: `"webdav"`)

* `wasabi` (value: `"wasabi"`)

* `backblaze_b2` (value: `"backblaze_b2"`)

* `one_drive` (value: `"one_drive"`)

* `rackspace` (value: `"rackspace"`)

* `box` (value: `"box"`)

* `dropbox` (value: `"dropbox"`)

* `google_drive` (value: `"google_drive"`)

* `azure` (value: `"azure"`)

* `sharepoint` (value: `"sharepoint"`)

* `s3_compatible` (value: `"s3_compatible"`)

* `azure_files` (value: `"azure_files"`)

* `files_agent` (value: `"files_agent"`)

* `filebase` (value: `"filebase"`)





## Enum: SsoStrategyTypeEnum


* `google` (value: `"google"`)

* `auth0` (value: `"auth0"`)

* `okta` (value: `"okta"`)

* `atlassian` (value: `"atlassian"`)

* `azure` (value: `"azure"`)

* `box` (value: `"box"`)

* `dropbox` (value: `"dropbox"`)

* `slack` (value: `"slack"`)

* `_unused_ubuntu` (value: `"_unused_ubuntu"`)

* `onelogin` (value: `"onelogin"`)

* `saml` (value: `"saml"`)

* `idaptive` (value: `"idaptive"`)

* `ldap` (value: `"ldap"`)

* `scim` (value: `"scim"`)




