

# AutomationRunbookReceiver

The Azure Automation Runbook notification receiver.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automationAccountId** | **String** | The Azure automation account Id which holds this runbook and authenticate to Azure resource. |  |
|**isGlobalRunbook** | **Boolean** | Indicates whether this instance is global runbook. |  |
|**name** | **String** | Indicates name of the webhook. |  [optional] |
|**runbookName** | **String** | The name for this runbook. |  |
|**serviceUri** | **String** | The URI where webhooks should be sent. |  [optional] |
|**webhookResourceId** | **String** | The resource id for webhook linked to this runbook. |  |



