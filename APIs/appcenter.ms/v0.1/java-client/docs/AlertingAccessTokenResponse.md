

# AlertingAccessTokenResponse

Access token details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokenId** | **String** | ID of the access token |  |
|**externalAccountName** | **String** | The account name of external user that used to authenticate against the external oauth provider or basic auth |  |
|**externalProviderName** | [**ExternalProviderNameEnum**](#ExternalProviderNameEnum) | External provider name |  |
|**externalUserEmail** | **String** | The email of external user that used to authenticate aginst the external oauth provider |  |



## Enum: ExternalProviderNameEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;github&quot; |
| VSTS | &quot;vsts&quot; |
| JIRA | &quot;jira&quot; |



