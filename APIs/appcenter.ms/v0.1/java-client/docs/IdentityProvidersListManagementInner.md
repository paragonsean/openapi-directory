

# IdentityProvidersListManagementInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | Creation date-time |  [optional] |
|**providerName** | [**ProviderNameEnum**](#ProviderNameEnum) | The name of the identity provider type |  [optional] |
|**providerUserId** | **String** | The external user id |  [optional] |
|**updatedAt** | **String** | Last update date-time |  [optional] |
|**userId** | **String** | The account id (UUID) |  [optional] |



## Enum: ProviderNameEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;github&quot; |
| AAD | &quot;aad&quot; |
| FACEBOOK | &quot;facebook&quot; |
| GOOGLE | &quot;google&quot; |



