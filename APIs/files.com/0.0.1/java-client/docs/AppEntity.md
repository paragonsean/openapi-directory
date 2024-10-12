

# AppEntity

List Apps

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appType** | [**AppTypeEnum**](#AppTypeEnum) | The type of the App |  [optional] |
|**documentationLinks** | **Object** | Collection of named links to documentation |  [optional] |
|**extendedDescription** | **String** | Long form description of the App |  [optional] |
|**externalHomepageUrl** | **String** | Link to external homepage |  [optional] |
|**featured** | **Boolean** | Is featured on the App listing? |  [optional] |
|**folderBehaviorType** | [**FolderBehaviorTypeEnum**](#FolderBehaviorTypeEnum) | Associated Folder Behavior type, if any |  [optional] |
|**iconUrl** | **String** | App icon |  [optional] |
|**logoThumbnailUrl** | **String** | Logo thumbnail for the App |  [optional] |
|**logoUrl** | **String** | Full size logo for the App |  [optional] |
|**marketingYoutubeUrl** | **String** | Marketing video page |  [optional] |
|**name** | **String** | Name of the App |  [optional] |
|**remoteServerType** | [**RemoteServerTypeEnum**](#RemoteServerTypeEnum) | Associated Remote Server type, if any |  [optional] |
|**screenshotListUrls** | **List&lt;String&gt;** | Screenshots of the App |  [optional] |
|**shortDescription** | **String** | Short description of the App |  [optional] |
|**ssoStrategyType** | [**SsoStrategyTypeEnum**](#SsoStrategyTypeEnum) | Associated SSO Strategy type, if any |  [optional] |
|**tutorialYoutubeUrl** | **String** | Tutorial video page |  [optional] |



## Enum: AppTypeEnum

| Name | Value |
|---- | -----|
| SDK | &quot;sdk&quot; |
| SSO | &quot;sso&quot; |
| REMOTE_SERVER | &quot;remote_server&quot; |
| FOLDER_BEHAVIOR | &quot;folder_behavior&quot; |
| CLIENT_APP | &quot;client_app&quot; |
| APP_INTEGRATION | &quot;app_integration&quot; |



## Enum: FolderBehaviorTypeEnum

| Name | Value |
|---- | -----|
| WEBHOOK | &quot;webhook&quot; |
| FILE_EXPIRATION | &quot;file_expiration&quot; |
| AUTO_ENCRYPT | &quot;auto_encrypt&quot; |
| LOCK_SUBFOLDERS | &quot;lock_subfolders&quot; |
| STORAGE_REGION | &quot;storage_region&quot; |
| SERVE_PUBLICLY | &quot;serve_publicly&quot; |
| CREATE_USER_FOLDERS | &quot;create_user_folders&quot; |
| REMOTE_SERVER_SYNC | &quot;remote_server_sync&quot; |
| INBOX | &quot;inbox&quot; |
| APPEND_TIMESTAMP | &quot;append_timestamp&quot; |
| LIMIT_FILE_EXTENSIONS | &quot;limit_file_extensions&quot; |
| LIMIT_FILE_REGEX | &quot;limit_file_regex&quot; |
| AMAZON_SNS | &quot;amazon_sns&quot; |
| WATERMARK | &quot;watermark&quot; |
| REMOTE_SERVER_MOUNT | &quot;remote_server_mount&quot; |
| SLACK_WEBHOOK | &quot;slack_webhook&quot; |
| AUTO_DECRYPT | &quot;auto_decrypt&quot; |
| OVERRIDE_UPLOAD_FILENAME | &quot;override_upload_filename&quot; |



## Enum: RemoteServerTypeEnum

| Name | Value |
|---- | -----|
| FTP | &quot;ftp&quot; |
| SFTP | &quot;sftp&quot; |
| S3 | &quot;s3&quot; |
| GOOGLE_CLOUD_STORAGE | &quot;google_cloud_storage&quot; |
| WEBDAV | &quot;webdav&quot; |
| WASABI | &quot;wasabi&quot; |
| BACKBLAZE_B2 | &quot;backblaze_b2&quot; |
| ONE_DRIVE | &quot;one_drive&quot; |
| RACKSPACE | &quot;rackspace&quot; |
| BOX | &quot;box&quot; |
| DROPBOX | &quot;dropbox&quot; |
| GOOGLE_DRIVE | &quot;google_drive&quot; |
| AZURE | &quot;azure&quot; |
| SHAREPOINT | &quot;sharepoint&quot; |
| S3_COMPATIBLE | &quot;s3_compatible&quot; |
| AZURE_FILES | &quot;azure_files&quot; |
| FILES_AGENT | &quot;files_agent&quot; |
| FILEBASE | &quot;filebase&quot; |



## Enum: SsoStrategyTypeEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| AUTH0 | &quot;auth0&quot; |
| OKTA | &quot;okta&quot; |
| ATLASSIAN | &quot;atlassian&quot; |
| AZURE | &quot;azure&quot; |
| BOX | &quot;box&quot; |
| DROPBOX | &quot;dropbox&quot; |
| SLACK | &quot;slack&quot; |
| _UNUSED_UBUNTU | &quot;_unused_ubuntu&quot; |
| ONELOGIN | &quot;onelogin&quot; |
| SAML | &quot;saml&quot; |
| IDAPTIVE | &quot;idaptive&quot; |
| LDAP | &quot;ldap&quot; |
| SCIM | &quot;scim&quot; |



