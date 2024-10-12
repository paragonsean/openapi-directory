

# ExportRequest

Export database parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administratorLogin** | **String** | The name of the SQL administrator. |  |
|**administratorLoginPassword** | **String** | The password of the SQL administrator. |  |
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | The authentication type. |  [optional] |
|**storageKey** | **String** | The storage key to use.  If storage key type is SharedAccessKey, it must be preceded with a \&quot;?.\&quot; |  |
|**storageKeyType** | [**StorageKeyTypeEnum**](#StorageKeyTypeEnum) | The type of the storage key to use. |  |
|**storageUri** | **String** | The storage uri to use. |  |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| SQL | &quot;SQL&quot; |
| AD_PASSWORD | &quot;ADPassword&quot; |



## Enum: StorageKeyTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCESS_KEY | &quot;StorageAccessKey&quot; |
| SHARED_ACCESS_KEY | &quot;SharedAccessKey&quot; |



