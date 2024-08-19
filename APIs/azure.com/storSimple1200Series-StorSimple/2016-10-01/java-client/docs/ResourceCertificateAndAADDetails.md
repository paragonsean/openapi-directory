

# ResourceCertificateAndAADDetails

Resource Certificate And AAD Details from IDM

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAuthority** | **String** | AAD tenant authority |  |
|**aadTenantId** | **String** | AAD tenant Id |  |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | Specify the Authentication type |  [optional] |
|**azureManagementEndpointAudience** | **String** | Azure Management Endpoint Audience |  |
|**certificate** | **String** | Gets or sets the base64 encoded certificate raw data string |  |
|**friendlyName** | **String** | Certificate friendly name |  |
|**issuer** | **String** | Certificate issuer |  |
|**resourceId** | **Long** | Gets or Sets the ResourceId |  |
|**servicePrincipalClientId** | **String** | AAD service principal clientId |  |
|**servicePrincipalObjectId** | **String** | AAD service principal ObjectId |  |
|**subject** | **String** | Certificate Subject Name |  |
|**thumbprint** | **String** | Certificate thumbprint |  |
|**validFrom** | **OffsetDateTime** | Certificate Validity start Date time |  |
|**validTo** | **OffsetDateTime** | Certificate Validity End Date time |  |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ACCESS_CONTROL_SERVICE | &quot;AccessControlService&quot; |
| AZURE_ACTIVE_DIRECTORY | &quot;AzureActiveDirectory&quot; |



