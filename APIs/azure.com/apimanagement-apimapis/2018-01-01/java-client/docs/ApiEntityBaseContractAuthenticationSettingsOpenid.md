

# ApiEntityBaseContractAuthenticationSettingsOpenid

API OAuth2 Authentication settings details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bearerTokenSendingMethods** | [**List&lt;BearerTokenSendingMethodsEnum&gt;**](#List&lt;BearerTokenSendingMethodsEnum&gt;) | How to send token to the server. |  [optional] |
|**openidProviderId** | **String** | OAuth authorization server identifier. |  [optional] |



## Enum: List&lt;BearerTokenSendingMethodsEnum&gt;

| Name | Value |
|---- | -----|
| AUTHORIZATION_HEADER | &quot;authorizationHeader&quot; |
| QUERY | &quot;query&quot; |



