

# UploadCertificateResponse

The upload registration certificate response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAudience** | **String** | Identifier of the target resource that is the recipient of the requested token. |  [optional] [readonly] |
|**aadAuthority** | **String** | Azure Active Directory tenant authority. |  [optional] [readonly] |
|**aadTenantId** | **String** | Azure Active Directory tenant ID. |  [optional] [readonly] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | Specifies authentication type. |  [optional] |
|**azureManagementEndpointAudience** | **String** | The azure management endpoint audience. |  [optional] [readonly] |
|**resourceId** | **String** | The resource ID of the Data Box Edge/Gateway device. |  [optional] [readonly] |
|**servicePrincipalClientId** | **String** | Azure Active Directory service principal client ID. |  [optional] [readonly] |
|**servicePrincipalObjectId** | **String** | Azure Active Directory service principal object ID. |  [optional] [readonly] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_ACTIVE_DIRECTORY | &quot;AzureActiveDirectory&quot; |



