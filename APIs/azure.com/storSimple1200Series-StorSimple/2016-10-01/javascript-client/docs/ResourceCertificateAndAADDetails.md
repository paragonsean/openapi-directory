# StorSimpleManagementClient.ResourceCertificateAndAADDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadAuthority** | **String** | AAD tenant authority | 
**aadTenantId** | **String** | AAD tenant Id | 
**authType** | **String** | Specify the Authentication type | [optional] 
**azureManagementEndpointAudience** | **String** | Azure Management Endpoint Audience | 
**certificate** | **String** | Gets or sets the base64 encoded certificate raw data string | 
**friendlyName** | **String** | Certificate friendly name | 
**issuer** | **String** | Certificate issuer | 
**resourceId** | **Number** | Gets or Sets the ResourceId | 
**servicePrincipalClientId** | **String** | AAD service principal clientId | 
**servicePrincipalObjectId** | **String** | AAD service principal ObjectId | 
**subject** | **String** | Certificate Subject Name | 
**thumbprint** | **String** | Certificate thumbprint | 
**validFrom** | **Date** | Certificate Validity start Date time | 
**validTo** | **Date** | Certificate Validity End Date time | 



## Enum: AuthTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AccessControlService` (value: `"AccessControlService"`)

* `AzureActiveDirectory` (value: `"AzureActiveDirectory"`)




