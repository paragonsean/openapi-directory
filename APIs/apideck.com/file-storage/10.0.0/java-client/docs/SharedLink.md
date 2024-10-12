

# SharedLink


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**downloadUrl** | **String** | The URL that can be used to download the file. |  [optional] |
|**expiresAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**password** | **String** | Optional password for the shared link. |  [optional] |
|**passwordProtected** | **Boolean** | Indicated if the shared link is password protected. |  [optional] [readonly] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The scope of the shared link. |  [optional] |
|**target** | [**SharedLinkTarget**](SharedLinkTarget.md) |  |  [optional] |
|**targetId** | **String** | The ID of the file or folder to link. |  |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**url** | **String** | The URL that can be used to view the file. |  [optional] [readonly] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| COMPANY | &quot;company&quot; |



