# ConfigurationWebhooks.CardOrderNotificationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CardOrderItem**](CardOrderItem.md) | Contains event details. | 
**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. | 
**type** | **String** | Type of webhook. | 



## Enum: TypeEnum


* `created` (value: `"balancePlatform.cardorder.created"`)

* `updated` (value: `"balancePlatform.cardorder.updated"`)




