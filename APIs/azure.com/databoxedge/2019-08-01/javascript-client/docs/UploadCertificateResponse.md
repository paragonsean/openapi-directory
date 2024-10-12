# DataBoxEdgeManagementClient.UploadCertificateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadAudience** | **String** | Identifier of the target resource that is the recipient of the requested token. | [optional] [readonly] 
**aadAuthority** | **String** | Azure Active Directory tenant authority. | [optional] [readonly] 
**aadTenantId** | **String** | Azure Active Directory tenant ID. | [optional] [readonly] 
**authType** | **String** | Specifies authentication type. | [optional] 
**azureManagementEndpointAudience** | **String** | The azure management endpoint audience. | [optional] [readonly] 
**resourceId** | **String** | The resource ID of the Data Box Edge/Gateway device. | [optional] [readonly] 
**servicePrincipalClientId** | **String** | Azure Active Directory service principal client ID. | [optional] [readonly] 
**servicePrincipalObjectId** | **String** | Azure Active Directory service principal object ID. | [optional] [readonly] 



## Enum: AuthTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureActiveDirectory` (value: `"AzureActiveDirectory"`)




