

# AuthorizationServerListByService200ResponseValueInnerProperties

External OAuth authorization server settings Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationEndpoint** | **String** | OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2. |  |
|**clientId** | **String** | Client or app id registered with this authorization server. |  |
|**clientRegistrationEndpoint** | **String** | Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. |  |
|**clientSecret** | **String** | Client or app secret registered with this authorization server. This property will not be filled on &#39;GET&#39; operations! Use &#39;/listSecrets&#39; POST request to get the value. |  [optional] |
|**displayName** | **String** | User-friendly authorization server name. |  |
|**grantTypes** | [**List&lt;GrantTypesEnum&gt;**](#List&lt;GrantTypesEnum&gt;) | Form of an authorization grant, which the client uses to request the access token. |  |



## Enum: List&lt;GrantTypesEnum&gt;

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorizationCode&quot; |
| IMPLICIT | &quot;implicit&quot; |
| RESOURCE_OWNER_PASSWORD | &quot;resourceOwnerPassword&quot; |
| CLIENT_CREDENTIALS | &quot;clientCredentials&quot; |



