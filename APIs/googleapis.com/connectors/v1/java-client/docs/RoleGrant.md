

# RoleGrant

This configuration defines all the Cloud IAM roles that needs to be granted to a particular Google Cloud resource for the selected principal like service account. These configurations will let UI display to customers what IAM roles need to be granted by them. Or these configurations can be used by the UI to render a 'grant' button to do the same on behalf of the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**helperTextTemplate** | **String** | Template that UI can use to provide helper text to customers. |  [optional] |
|**principal** | [**PrincipalEnum**](#PrincipalEnum) | Prinicipal/Identity for whom the role need to assigned. |  [optional] |
|**resource** | [**Resource**](Resource.md) |  |  [optional] |
|**roles** | **List&lt;String&gt;** | List of roles that need to be granted. |  [optional] |



## Enum: PrincipalEnum

| Name | Value |
|---- | -----|
| PRINCIPAL_UNSPECIFIED | &quot;PRINCIPAL_UNSPECIFIED&quot; |
| CONNECTOR_SA | &quot;CONNECTOR_SA&quot; |



