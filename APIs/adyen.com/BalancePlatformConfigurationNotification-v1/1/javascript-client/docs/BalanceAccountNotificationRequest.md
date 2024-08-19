# ConfigurationWebhooks.BalanceAccountNotificationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BalanceAccountNotificationData**](BalanceAccountNotificationData.md) | Contains event details. | 
**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. | 
**type** | **String** | Type of webhook. | 



## Enum: TypeEnum


* `updated` (value: `"balancePlatform.balanceAccount.updated"`)

* `created` (value: `"balancePlatform.balanceAccount.created"`)




