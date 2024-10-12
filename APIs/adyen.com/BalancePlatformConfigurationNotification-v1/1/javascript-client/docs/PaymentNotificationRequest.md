# ConfigurationWebhooks.PaymentNotificationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaymentInstrumentNotificationData**](PaymentInstrumentNotificationData.md) | Contains event details. | 
**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. | 
**type** | **String** | Type of webhook. | 



## Enum: TypeEnum


* `created` (value: `"balancePlatform.paymentInstrument.created"`)

* `updated` (value: `"balancePlatform.paymentInstrument.updated"`)




