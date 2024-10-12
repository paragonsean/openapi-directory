# ConfigurationWebhooks.SweepConfigurationNotificationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SweepConfigurationNotificationData**](SweepConfigurationNotificationData.md) | Contains event details. | 
**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. | 
**type** | **String** | Type of webhook. | 



## Enum: TypeEnum


* `created` (value: `"balancePlatform.balanceAccountSweep.created"`)

* `updated` (value: `"balancePlatform.balanceAccountSweep.updated"`)

* `deleted` (value: `"balancePlatform.balanceAccountSweep.deleted"`)




