# ManagedServiceIdentityClient.IdentityProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | The id of the app associated with the identity. This is a random generated UUID by MSI. | [optional] [readonly] 
**clientSecretUrl** | **String** |  The ManagedServiceIdentity DataPlane URL that can be queried to obtain the identity credentials. | [optional] [readonly] 
**principalId** | **String** | The id of the service principal object associated with the created identity. | [optional] [readonly] 
**tenantId** | **String** | The id of the tenant which the identity belongs to. | [optional] [readonly] 


