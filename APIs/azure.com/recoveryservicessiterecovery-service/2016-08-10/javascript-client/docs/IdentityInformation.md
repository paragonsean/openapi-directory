# SiteRecoveryManagementClient.IdentityInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadAuthority** | **String** | The base authority for Azure Active Directory authentication. | [optional] 
**applicationId** | **String** | The application/client Id for the service principal with which the on-premise management/data plane components would communicate with our Azure services. | [optional] 
**audience** | **String** | The intended Audience of the service principal with which the on-premise management/data plane components would communicate with our Azure services. | [optional] 
**certificateThumbprint** | **String** | The certificate thumbprint. Applicable only if IdentityProviderType is RecoveryServicesActiveDirectory. | [optional] 
**identityProviderType** | **String** | The identity provider type. Value is the ToString() of a IdentityProviderType value. | [optional] 
**objectId** | **String** | The object Id of the service principal with which the on-premise management/data plane components would communicate with our Azure services. | [optional] 
**tenantId** | **String** | The tenant Id for the service principal with which the on-premise management/data plane components would communicate with our Azure services. | [optional] 



## Enum: IdentityProviderTypeEnum


* `RecoveryServicesActiveDirectory` (value: `"RecoveryServicesActiveDirectory"`)

* `CustomerActiveDirectory` (value: `"CustomerActiveDirectory"`)




