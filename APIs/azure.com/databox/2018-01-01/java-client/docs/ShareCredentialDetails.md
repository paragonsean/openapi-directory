

# ShareCredentialDetails

Credential details of the shares in account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**password** | **String** | Password for the share. |  [optional] [readonly] |
|**shareName** | **String** | Name of the share. |  [optional] [readonly] |
|**shareType** | [**ShareTypeEnum**](#ShareTypeEnum) | Type of the share. |  [optional] [readonly] |
|**supportedAccessProtocols** | [**List&lt;SupportedAccessProtocolsEnum&gt;**](#List&lt;SupportedAccessProtocolsEnum&gt;) | Access protocols supported on the device. |  [optional] [readonly] |
|**userName** | **String** | User name for the share. |  [optional] [readonly] |



## Enum: ShareTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_TYPE | &quot;UnknownType&quot; |
| HCS | &quot;HCS&quot; |
| BLOCK_BLOB | &quot;BlockBlob&quot; |
| PAGE_BLOB | &quot;PageBlob&quot; |
| AZURE_FILE | &quot;AzureFile&quot; |
| MANAGED_DISK | &quot;ManagedDisk&quot; |



## Enum: List&lt;SupportedAccessProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| SMB | &quot;SMB&quot; |
| NFS | &quot;NFS&quot; |



