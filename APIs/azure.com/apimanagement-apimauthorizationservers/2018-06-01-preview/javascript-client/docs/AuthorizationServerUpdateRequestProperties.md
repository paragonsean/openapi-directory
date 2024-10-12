# ApiManagementClient.AuthorizationServerUpdateRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEndpoint** | **String** | OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2. | [optional] 
**clientId** | **String** | Client or app id registered with this authorization server. | [optional] 
**clientRegistrationEndpoint** | **String** | Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. | [optional] 
**displayName** | **String** | User-friendly authorization server name. | [optional] 
**grantTypes** | **[String]** | Form of an authorization grant, which the client uses to request the access token. | [optional] 



## Enum: [GrantTypesEnum]


* `authorizationCode` (value: `"authorizationCode"`)

* `implicit` (value: `"implicit"`)

* `resourceOwnerPassword` (value: `"resourceOwnerPassword"`)

* `clientCredentials` (value: `"clientCredentials"`)




