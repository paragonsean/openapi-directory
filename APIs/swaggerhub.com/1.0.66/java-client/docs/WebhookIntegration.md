

# WebhookIntegration

Configuration details for [webhooks](https://support.smartbear.com/swaggerhub/docs/integrations/webhook.html)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**additionalHeaders** | **List&lt;String&gt;** | Custom HTTP headers to be sent with the webhook. Use the \&quot;name: value\&quot; format for each header. |  [optional] |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Webhook content type |  |
|**lifeCycleEvents** | [**List&lt;LifeCycleEventsEnum&gt;**](#List&lt;LifeCycleEventsEnum&gt;) | Events that will trigger the webhook |  [optional] |
|**url** | **URI** | The URL to send the webhook to |  |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| WEBHOOK | &quot;WEBHOOK&quot; |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| JSON | &quot;application/json&quot; |
| X_WWW_FORM_URLENCODED | &quot;application/x-www-form-urlencoded&quot; |



## Enum: List&lt;LifeCycleEventsEnum&gt;

| Name | Value |
|---- | -----|
| SAVED | &quot;API_SAVED&quot; |
| PUBLISHED | &quot;API_PUBLISHED&quot; |



