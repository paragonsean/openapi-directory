

# AutoMockingIntegration

Configuration details for the [API Auto Mocking](https://support.smartbear.com/swaggerhub/docs/integrations/api-auto-mocking.html) integration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**defaultResponseType** | [**DefaultResponseTypeEnum**](#DefaultResponseTypeEnum) | Response content type that the mock server will return if no &#x60;Accept&#x60; header is specified. |  [optional] |
|**modify** | **Boolean** | Whether to update the &#x60;host&#x60;/&#x60;servers&#x60; in the API definition to point to the mock server. &#x60;modify&#x60;&#x3D;&#x60;true&#x60; can only be used if the API is _unpublished_. |  [optional] |
|**token** | **String** | (For private APIs only.) An arbitrary bearer token that the users will need to send in requests to the mock server. |  [optional] |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| API_AUTO_MOCKING | &quot;API_AUTO_MOCKING&quot; |



## Enum: DefaultResponseTypeEnum

| Name | Value |
|---- | -----|
| JSON | &quot;application/json&quot; |
| XML | &quot;application/xml&quot; |
| YAML | &quot;application/yaml&quot; |



