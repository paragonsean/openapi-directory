

# AuthorizationServerUpdateRequestProperties

External OAuth authorization server Update settings contract.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationEndpoint** | **String** | OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2. |  [optional] |
|**clientId** | **String** | Client or app id registered with this authorization server. |  [optional] |
|**clientRegistrationEndpoint** | **String** | Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. |  [optional] |
|**displayName** | **String** | User-friendly authorization server name. |  [optional] |
|**grantTypes** | [**List&lt;GrantTypesEnum&gt;**](#List&lt;GrantTypesEnum&gt;) | Form of an authorization grant, which the client uses to request the access token. |  [optional] |



## Enum: List&lt;GrantTypesEnum&gt;

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorizationCode&quot; |
| IMPLICIT | &quot;implicit&quot; |
| RESOURCE_OWNER_PASSWORD | &quot;resourceOwnerPassword&quot; |
| CLIENT_CREDENTIALS | &quot;clientCredentials&quot; |



