

# CardOrderNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**CardOrderItem**](CardOrderItem.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;balancePlatform.cardorder.created&quot; |
| UPDATED | &quot;balancePlatform.cardorder.updated&quot; |



