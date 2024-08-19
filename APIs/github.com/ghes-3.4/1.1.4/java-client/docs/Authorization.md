

# Authorization

The authorization for an OAuth app, GitHub App, or a Personal Access Token.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**app** | [**ApplicationGrantApp**](ApplicationGrantApp.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**expiresAt** | **OffsetDateTime** |  |  |
|**fingerprint** | **String** |  |  |
|**hashedToken** | **String** |  |  |
|**id** | **Integer** |  |  |
|**installation** | [**NullableScopedInstallation**](NullableScopedInstallation.md) |  |  [optional] |
|**note** | **String** |  |  |
|**noteUrl** | **URI** |  |  |
|**scopes** | **List&lt;String&gt;** | A list of scopes that this authorization is in. |  |
|**token** | **String** |  |  |
|**tokenLastEight** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |



