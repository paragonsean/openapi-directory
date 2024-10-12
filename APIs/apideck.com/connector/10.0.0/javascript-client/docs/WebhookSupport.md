# ConnectorApi.WebhookSupport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managedVia** | **String** | How the subscription is managed in the downstream. | [optional] 
**mode** | **String** | Mode of the webhook support. | [optional] 
**subscriptionLevel** | **String** | Received events are scoped to connection or across integration. | [optional] 
**virtualWebhooks** | [**VirtualWebhooks**](VirtualWebhooks.md) |  | [optional] 



## Enum: ManagedViaEnum


* `manual` (value: `"manual"`)

* `api` (value: `"api"`)





## Enum: ModeEnum


* `native` (value: `"native"`)

* `virtual` (value: `"virtual"`)

* `none` (value: `"none"`)





## Enum: SubscriptionLevelEnum


* `connection` (value: `"connection"`)

* `integration` (value: `"integration"`)




