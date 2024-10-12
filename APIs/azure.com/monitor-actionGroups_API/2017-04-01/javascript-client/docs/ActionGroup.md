# AzureActionGroups.ActionGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automationRunbookReceivers** | [**[AutomationRunbookReceiver]**](AutomationRunbookReceiver.md) | The list of AutomationRunbook receivers that are part of this action group. | [optional] 
**azureAppPushReceivers** | [**[AzureAppPushReceiver]**](AzureAppPushReceiver.md) | The list of AzureAppPush receivers that are part of this action group. | [optional] 
**emailReceivers** | [**[EmailReceiver]**](EmailReceiver.md) | The list of email receivers that are part of this action group. | [optional] 
**enabled** | **Boolean** | Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. | [default to true]
**groupShortName** | **String** | The short name of the action group. This will be used in SMS messages. | 
**itsmReceivers** | [**[ItsmReceiver]**](ItsmReceiver.md) | The list of ITSM receivers that are part of this action group. | [optional] 
**smsReceivers** | [**[SmsReceiver]**](SmsReceiver.md) | The list of SMS receivers that are part of this action group. | [optional] 
**webhookReceivers** | [**[WebhookReceiver]**](WebhookReceiver.md) | The list of webhook receivers that are part of this action group. | [optional] 


