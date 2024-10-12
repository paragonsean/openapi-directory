# SwaggerHubRegistryApi.WebhookIntegration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the integration is enabled or disabled | [optional] [default to true]
**id** | **String** | ID of the integration | [optional] [readonly] 
**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. | 
**additionalHeaders** | **[String]** | Custom HTTP headers to be sent with the webhook. Use the \&quot;name: value\&quot; format for each header. | [optional] 
**configType** | **String** | Integration type | 
**contentType** | **String** | Webhook content type | 
**lifeCycleEvents** | **[String]** | Events that will trigger the webhook | [optional] 
**url** | **String** | The URL to send the webhook to | 



## Enum: ConfigTypeEnum


* `WEBHOOK` (value: `"WEBHOOK"`)





## Enum: ContentTypeEnum


* `json` (value: `"application/json"`)

* `x-www-form-urlencoded` (value: `"application/x-www-form-urlencoded"`)





## Enum: [LifeCycleEventsEnum]


* `SAVED` (value: `"API_SAVED"`)

* `PUBLISHED` (value: `"API_PUBLISHED"`)




