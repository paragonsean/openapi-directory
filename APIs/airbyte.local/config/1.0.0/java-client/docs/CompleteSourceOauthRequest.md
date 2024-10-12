

# CompleteSourceOauthRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**oAuthInputConfiguration** | **Object** | The values required to configure OAuth flows. The schema for this must match the &#x60;OAuthConfigSpecification.oauthUserInputFromConnectorConfigSpecification&#x60; schema. |  [optional] |
|**queryParams** | **Map&lt;String, Object&gt;** | The query parameters present in the redirect URL after a user granted consent e.g auth code |  [optional] |
|**redirectUrl** | **String** | When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given. |  [optional] |
|**sourceDefinitionId** | **UUID** |  |  |
|**sourceId** | **UUID** |  |  [optional] |
|**workspaceId** | **UUID** |  |  |



