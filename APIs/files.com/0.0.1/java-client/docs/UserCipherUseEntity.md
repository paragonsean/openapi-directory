

# UserCipherUseEntity

List User Cipher Uses

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The earliest recorded use of this combination of interface and protocol and cipher (for this user) |  [optional] |
|**id** | **Integer** | UserCipherUse ID |  [optional] |
|**_interface** | [**InterfaceEnum**](#InterfaceEnum) | The interface accessed |  [optional] |
|**protocolCipher** | **String** | The protocol and cipher employed |  [optional] |
|**updatedAt** | **OffsetDateTime** | The most recent use of this combination of interface and protocol and cipher (for this user) |  [optional] |
|**userId** | **Integer** | ID of the user who performed this access |  [optional] |



## Enum: InterfaceEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| FTP | &quot;ftp&quot; |
| SFTP | &quot;sftp&quot; |
| DAV | &quot;dav&quot; |
| DESKTOP | &quot;desktop&quot; |
| RESTAPI | &quot;restapi&quot; |
| ROBOT | &quot;robot&quot; |
| JSAPI | &quot;jsapi&quot; |



