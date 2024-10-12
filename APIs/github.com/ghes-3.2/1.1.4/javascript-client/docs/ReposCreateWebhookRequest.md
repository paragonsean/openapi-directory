# GitHubV3RestApi.ReposCreateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to true]
**config** | [**ReposCreateWebhookRequestConfig**](ReposCreateWebhookRequestConfig.md) |  | [optional] 
**events** | **[String]** | Determines what [events](https://docs.github.com/enterprise-server@3.2/webhooks/event-payloads) the hook is triggered for. | [optional] 
**name** | **String** | Use &#x60;web&#x60; to create a webhook. Default: &#x60;web&#x60;. This parameter only accepts the value &#x60;web&#x60;. | [optional] 


