# FilesComApi.RemoteServerEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authAccountName** | **String** | Describes the authorized account | [optional] 
**authSetupLink** | **String** | Returns link to login with an Oauth provider | [optional] 
**authStatus** | **String** | Either &#x60;in_setup&#x60; or &#x60;complete&#x60; | [optional] 
**authenticationMethod** | **String** | Type of authentication method | [optional] 
**awsAccessKey** | **String** | AWS Access Key. | [optional] 
**azureBlobStorageAccount** | **String** | Azure Blob Storage Account name | [optional] 
**azureBlobStorageContainer** | **String** | Azure Blob Storage Container name | [optional] 
**azureBlobStorageSasToken** | **String** | Shared Access Signature (SAS) token | [optional] 
**azureFilesStorageAccount** | **String** | Azure File Storage Account name | [optional] 
**azureFilesStorageSasToken** | **String** | Shared Access Signature (SAS) token | [optional] 
**azureFilesStorageShareName** | **String** | Azure File Storage Share name | [optional] 
**backblazeB2Bucket** | **String** | Backblaze B2 Cloud Storage Bucket name | [optional] 
**backblazeB2S3Endpoint** | **String** | Backblaze B2 Cloud Storage S3 Endpoint | [optional] 
**disabled** | **Boolean** | If true, this server has been disabled due to failures.  Make any change or set disabled to false to clear this flag. | [optional] 
**enableDedicatedIps** | **Boolean** | &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] 
**filebaseAccessKey** | **String** | Filebase Access Key. | [optional] 
**filebaseBucket** | **String** | Filebase Bucket name | [optional] 
**filesAgentApiToken** | **String** | Files Agent API Token | [optional] 
**filesAgentPermissionSet** | **String** | Local permissions for files agent. read_only, write_only, or read_write | [optional] 
**filesAgentRoot** | **String** | Agent local root path | [optional] 
**googleCloudStorageBucket** | **String** | Google Cloud Storage bucket name | [optional] 
**googleCloudStorageProjectId** | **String** | Google Cloud Project ID | [optional] 
**hostname** | **String** | Hostname or IP address | [optional] 
**id** | **Number** | Remote server ID | [optional] 
**maxConnections** | **Number** | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). | [optional] 
**name** | **String** | Internal name for your reference | [optional] 
**oneDriveAccountType** | **String** | Either personal or business_other account types | [optional] 
**pinToSiteRegion** | **Boolean** | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. | [optional] 
**pinnedRegion** | **String** | If set, all communciations with this remote server are made through the provided region. | [optional] 
**port** | **Number** | Port for remote server.  Not needed for S3. | [optional] 
**rackspaceContainer** | **String** | The name of the container (top level directory) where files will sync. | [optional] 
**rackspaceRegion** | **String** | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ | [optional] 
**rackspaceUsername** | **String** | Rackspace username used to login to the Rackspace Cloud Control Panel. | [optional] 
**remoteHomePath** | **String** | Initial home folder on remote server | [optional] 
**s3Bucket** | **String** | S3 bucket name | [optional] 
**s3CompatibleAccessKey** | **String** | S3-compatible Access Key. | [optional] 
**s3CompatibleBucket** | **String** | S3-compatible Bucket name | [optional] 
**s3CompatibleEndpoint** | **String** | S3-compatible endpoint | [optional] 
**s3CompatibleRegion** | **String** | S3-compatible endpoint | [optional] 
**s3Region** | **String** | S3 region | [optional] 
**serverCertificate** | **String** | Remote server certificate | [optional] 
**serverHostKey** | **String** | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts | [optional] 
**serverType** | **String** | Remote server type. | [optional] 
**ssl** | **String** | Should we require SSL? | [optional] 
**username** | **String** | Remote server username.  Not needed for S3 buckets. | [optional] 
**wasabiAccessKey** | **String** | Wasabi access key. | [optional] 
**wasabiBucket** | **String** | Wasabi Bucket name | [optional] 
**wasabiRegion** | **String** | Wasabi region | [optional] 



## Enum: AuthStatusEnum


* `not_applicable` (value: `"not_applicable"`)

* `in_setup` (value: `"in_setup"`)

* `complete` (value: `"complete"`)

* `reauthenticate` (value: `"reauthenticate"`)





## Enum: FilesAgentPermissionSetEnum


* `read_write` (value: `"read_write"`)

* `read_only` (value: `"read_only"`)

* `write_only` (value: `"write_only"`)





## Enum: OneDriveAccountTypeEnum


* `personal` (value: `"personal"`)

* `business_other` (value: `"business_other"`)





## Enum: ServerCertificateEnum


* `require_match` (value: `"require_match"`)

* `allow_any` (value: `"allow_any"`)





## Enum: ServerTypeEnum


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





## Enum: SslEnum


* `if_available` (value: `"if_available"`)

* `require` (value: `"require"`)

* `require_implicit` (value: `"require_implicit"`)

* `never` (value: `"never"`)




