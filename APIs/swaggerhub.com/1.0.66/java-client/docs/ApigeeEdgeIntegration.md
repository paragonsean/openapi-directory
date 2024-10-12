

# ApigeeEdgeIntegration

Configuration details for the [Apigee Edge](https://support.smartbear.com/swaggerhub/docs/integrations/apigee-edge.html) integration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**apiName** | **String** | Name for the API that is going to be saved in your Apigee account |  |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**email** | **String** | Email address of your Apigee account |  |
|**host** | **String** | Apigee Edge Management instance URL. Use the default URL &#x60;https://api.enterprise.apigee.com/v1&#x60; for the cloud version of Apigee Edge. If using an On-Premise deployment, enter the URL to your Edge instance. |  [optional] |
|**organization** | **String** | Organization where the API will be saved |  |
|**password** | **String** | Password of your Apigee account. Write-only property. Required to create and update the integration. |  [optional] |
|**targetUrl** | **String** | Target endpoint for proxy |  |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| APIGEE_EDGE | &quot;APIGEE_EDGE&quot; |



