# DataBoxManagementClient.ShareCredentialDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **String** | Password for the share. | [optional] [readonly] 
**shareName** | **String** | Name of the share. | [optional] [readonly] 
**shareType** | **String** | Type of the share. | [optional] [readonly] 
**supportedAccessProtocols** | **[String]** | Access protocols supported on the device. | [optional] [readonly] 
**userName** | **String** | User name for the share. | [optional] [readonly] 



## Enum: ShareTypeEnum


* `UnknownType` (value: `"UnknownType"`)

* `HCS` (value: `"HCS"`)

* `BlockBlob` (value: `"BlockBlob"`)

* `PageBlob` (value: `"PageBlob"`)

* `AzureFile` (value: `"AzureFile"`)

* `ManagedDisk` (value: `"ManagedDisk"`)





## Enum: [SupportedAccessProtocolsEnum]


* `SMB` (value: `"SMB"`)

* `NFS` (value: `"NFS"`)




