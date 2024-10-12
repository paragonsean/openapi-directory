

# IdentityProperties

The properties associated with the identity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **UUID** | The id of the app associated with the identity. This is a random generated UUID by MSI. |  [optional] [readonly] |
|**clientSecretUrl** | **String** |  The ManagedServiceIdentity DataPlane URL that can be queried to obtain the identity credentials. If identity is user assigned, then the clientSecretUrl will not be present in the response, otherwise it will be present. |  [optional] [readonly] |
|**principalId** | **UUID** | The id of the service principal object associated with the created identity. |  [optional] [readonly] |
|**tenantId** | **UUID** | The id of the tenant which the identity belongs to. |  [optional] [readonly] |



