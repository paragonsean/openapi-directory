

# UploadCertificateResponse

The upload registration certificate response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAuthority** | **String** | Azure Active Directory tenant authority. |  |
|**aadTenantId** | **String** | Azure Active Directory tenant ID. |  |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | Specifies authentication type. |  [optional] |
|**azureManagementEndpointAudience** | **String** | The azure management endpoint audience. |  |
|**resourceId** | **String** | The resource ID of the Data Box Edge/Gateway device. |  |
|**servicePrincipalClientId** | **String** | Azure Active Directory service principal client ID. |  |
|**servicePrincipalObjectId** | **String** | Azure Active Directory service principal object ID. |  |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_ACTIVE_DIRECTORY | &quot;AzureActiveDirectory&quot; |



