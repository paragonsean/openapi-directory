# ServiceFabricClientApis.IdentityDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | the object identifier of the Service Principal of the identity associated with this resource. | [optional] 
**tenantId** | **String** | the identifier of the tenant containing the application&#39;s identity. | [optional] 
**tokenServiceEndpoint** | **String** | the endpoint for the token service managing this identity | [optional] 
**type** | **String** | the types of identities associated with this resource; currently restricted to &#39;SystemAssigned and UserAssigned&#39; | 
**userAssignedIdentities** | [**{String: IdentityItemDescription}**](IdentityItemDescription.md) | Defines a map that contains user assigned identities. | [optional] 


