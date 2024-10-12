

# RemoteServerEntity

Create Remote Server

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authAccountName** | **String** | Describes the authorized account |  [optional] |
|**authSetupLink** | **String** | Returns link to login with an Oauth provider |  [optional] |
|**authStatus** | [**AuthStatusEnum**](#AuthStatusEnum) | Either &#x60;in_setup&#x60; or &#x60;complete&#x60; |  [optional] |
|**authenticationMethod** | **String** | Type of authentication method |  [optional] |
|**awsAccessKey** | **String** | AWS Access Key. |  [optional] |
|**azureBlobStorageAccount** | **String** | Azure Blob Storage Account name |  [optional] |
|**azureBlobStorageContainer** | **String** | Azure Blob Storage Container name |  [optional] |
|**azureBlobStorageSasToken** | **String** | Shared Access Signature (SAS) token |  [optional] |
|**azureFilesStorageAccount** | **String** | Azure File Storage Account name |  [optional] |
|**azureFilesStorageSasToken** | **String** | Shared Access Signature (SAS) token |  [optional] |
|**azureFilesStorageShareName** | **String** | Azure File Storage Share name |  [optional] |
|**backblazeB2Bucket** | **String** | Backblaze B2 Cloud Storage Bucket name |  [optional] |
|**backblazeB2S3Endpoint** | **String** | Backblaze B2 Cloud Storage S3 Endpoint |  [optional] |
|**disabled** | **Boolean** | If true, this server has been disabled due to failures.  Make any change or set disabled to false to clear this flag. |  [optional] |
|**enableDedicatedIps** | **Boolean** | &#x60;true&#x60; if remote server only accepts connections from dedicated IPs |  [optional] |
|**filebaseAccessKey** | **String** | Filebase Access Key. |  [optional] |
|**filebaseBucket** | **String** | Filebase Bucket name |  [optional] |
|**filesAgentApiToken** | **String** | Files Agent API Token |  [optional] |
|**filesAgentPermissionSet** | [**FilesAgentPermissionSetEnum**](#FilesAgentPermissionSetEnum) | Local permissions for files agent. read_only, write_only, or read_write |  [optional] |
|**filesAgentRoot** | **String** | Agent local root path |  [optional] |
|**googleCloudStorageBucket** | **String** | Google Cloud Storage bucket name |  [optional] |
|**googleCloudStorageProjectId** | **String** | Google Cloud Project ID |  [optional] |
|**hostname** | **String** | Hostname or IP address |  [optional] |
|**id** | **Integer** | Remote server ID |  [optional] |
|**maxConnections** | **Integer** | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). |  [optional] |
|**name** | **String** | Internal name for your reference |  [optional] |
|**oneDriveAccountType** | [**OneDriveAccountTypeEnum**](#OneDriveAccountTypeEnum) | Either personal or business_other account types |  [optional] |
|**pinToSiteRegion** | **Boolean** | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. |  [optional] |
|**pinnedRegion** | **String** | If set, all communciations with this remote server are made through the provided region. |  [optional] |
|**port** | **Integer** | Port for remote server.  Not needed for S3. |  [optional] |
|**rackspaceContainer** | **String** | The name of the container (top level directory) where files will sync. |  [optional] |
|**rackspaceRegion** | **String** | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ |  [optional] |
|**rackspaceUsername** | **String** | Rackspace username used to login to the Rackspace Cloud Control Panel. |  [optional] |
|**remoteHomePath** | **String** | Initial home folder on remote server |  [optional] |
|**s3Bucket** | **String** | S3 bucket name |  [optional] |
|**s3CompatibleAccessKey** | **String** | S3-compatible Access Key. |  [optional] |
|**s3CompatibleBucket** | **String** | S3-compatible Bucket name |  [optional] |
|**s3CompatibleEndpoint** | **String** | S3-compatible endpoint |  [optional] |
|**s3CompatibleRegion** | **String** | S3-compatible endpoint |  [optional] |
|**s3Region** | **String** | S3 region |  [optional] |
|**serverCertificate** | [**ServerCertificateEnum**](#ServerCertificateEnum) | Remote server certificate |  [optional] |
|**serverHostKey** | **String** | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts |  [optional] |
|**serverType** | [**ServerTypeEnum**](#ServerTypeEnum) | Remote server type. |  [optional] |
|**ssl** | [**SslEnum**](#SslEnum) | Should we require SSL? |  [optional] |
|**username** | **String** | Remote server username.  Not needed for S3 buckets. |  [optional] |
|**wasabiAccessKey** | **String** | Wasabi access key. |  [optional] |
|**wasabiBucket** | **String** | Wasabi Bucket name |  [optional] |
|**wasabiRegion** | **String** | Wasabi region |  [optional] |



## Enum: AuthStatusEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;not_applicable&quot; |
| IN_SETUP | &quot;in_setup&quot; |
| COMPLETE | &quot;complete&quot; |
| REAUTHENTICATE | &quot;reauthenticate&quot; |



## Enum: FilesAgentPermissionSetEnum

| Name | Value |
|---- | -----|
| READ_WRITE | &quot;read_write&quot; |
| READ_ONLY | &quot;read_only&quot; |
| WRITE_ONLY | &quot;write_only&quot; |



## Enum: OneDriveAccountTypeEnum

| Name | Value |
|---- | -----|
| PERSONAL | &quot;personal&quot; |
| BUSINESS_OTHER | &quot;business_other&quot; |



## Enum: ServerCertificateEnum

| Name | Value |
|---- | -----|
| REQUIRE_MATCH | &quot;require_match&quot; |
| ALLOW_ANY | &quot;allow_any&quot; |



## Enum: ServerTypeEnum

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



## Enum: SslEnum

| Name | Value |
|---- | -----|
| IF_AVAILABLE | &quot;if_available&quot; |
| REQUIRE | &quot;require&quot; |
| REQUIRE_IMPLICIT | &quot;require_implicit&quot; |
| NEVER | &quot;never&quot; |



