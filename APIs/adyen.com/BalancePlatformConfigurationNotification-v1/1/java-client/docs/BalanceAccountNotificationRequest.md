

# BalanceAccountNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**BalanceAccountNotificationData**](BalanceAccountNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UPDATED | &quot;balancePlatform.balanceAccount.updated&quot; |
| CREATED | &quot;balancePlatform.balanceAccount.created&quot; |



