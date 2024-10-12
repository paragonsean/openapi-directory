

# ActionGroup

An Azure action group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automationRunbookReceivers** | [**List&lt;AutomationRunbookReceiver&gt;**](AutomationRunbookReceiver.md) | The list of AutomationRunbook receivers that are part of this action group. |  [optional] |
|**azureAppPushReceivers** | [**List&lt;AzureAppPushReceiver&gt;**](AzureAppPushReceiver.md) | The list of AzureAppPush receivers that are part of this action group. |  [optional] |
|**emailReceivers** | [**List&lt;EmailReceiver&gt;**](EmailReceiver.md) | The list of email receivers that are part of this action group. |  [optional] |
|**enabled** | **Boolean** | Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. |  |
|**groupShortName** | **String** | The short name of the action group. This will be used in SMS messages. |  |
|**itsmReceivers** | [**List&lt;ItsmReceiver&gt;**](ItsmReceiver.md) | The list of ITSM receivers that are part of this action group. |  [optional] |
|**smsReceivers** | [**List&lt;SmsReceiver&gt;**](SmsReceiver.md) | The list of SMS receivers that are part of this action group. |  [optional] |
|**webhookReceivers** | [**List&lt;WebhookReceiver&gt;**](WebhookReceiver.md) | The list of webhook receivers that are part of this action group. |  [optional] |



