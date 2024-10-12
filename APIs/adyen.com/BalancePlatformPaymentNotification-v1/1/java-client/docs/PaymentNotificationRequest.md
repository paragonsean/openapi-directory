

# PaymentNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**PaymentNotificationData**](PaymentNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;balancePlatform.payment.created&quot; |
| UPDATED | &quot;balancePlatform.payment.updated&quot; |



