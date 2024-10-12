

# AccountHolderNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**AccountHolderNotificationData**](AccountHolderNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UPDATED | &quot;balancePlatform.accountHolder.updated&quot; |
| CREATED | &quot;balancePlatform.accountHolder.created&quot; |



