

# AzureApiManagementIntegration

Configuration details for the [Azure API Management](https://support.smartbear.com/swaggerhub/docs/integrations/azure-api-management.html) integration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**apiId** | **String** | A unique identifier that allows you to connect your definition to an existing API. If left blank, a unique identifier will be added using an extension, &#x60;x-azure-api-id&#x60;. This value will be ignored if a value exists in the definition.  |  [optional] |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**serviceInstance** | **String** | The name of the Azure API Management service instance as it appears in the \&quot;All resources\&quot; list in the Azure portal  |  |
|**token** | **String** | A personal access token for accessing the Azure API Management service. Documentation for generating tokens is here:  https://docs.microsoft.com/en-us/rest/api/apimanagement/apimanagementrest/azure-api-management-rest-api-authentication Write-only property. Required to create and update the integration.  |  [optional] |
|**urlSuffix** | **String** | This suffix will be appended to the hostname of your API Management service instance to create a public URL for your API |  [optional] |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| AZURE_API_MANAGEMENT | &quot;AZURE_API_MANAGEMENT&quot; |



