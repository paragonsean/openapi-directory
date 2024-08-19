# GitHubV3RestApi.EnterpriseAdminCreateGlobalWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to true]
**config** | [**EnterpriseAdminCreateGlobalWebhookRequestConfig**](EnterpriseAdminCreateGlobalWebhookRequestConfig.md) |  | 
**events** | **[String]** | The [events](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads) that trigger this webhook. A global webhook can be triggered by &#x60;user&#x60; and &#x60;organization&#x60; events. Default: &#x60;user&#x60; and &#x60;organization&#x60;. | [optional] 
**name** | **String** | Must be passed as \&quot;web\&quot;. | 


