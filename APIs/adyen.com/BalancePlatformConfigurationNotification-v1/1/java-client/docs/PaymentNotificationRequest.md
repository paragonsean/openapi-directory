

# PaymentNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**PaymentInstrumentNotificationData**](PaymentInstrumentNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;balancePlatform.paymentInstrument.created&quot; |
| UPDATED | &quot;balancePlatform.paymentInstrument.updated&quot; |



