

# IncomingTransferNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**IncomingTransferNotificationData**](IncomingTransferNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UPDATED | &quot;balancePlatform.incomingTransfer.updated&quot; |
| CREATED | &quot;balancePlatform.incomingTransfer.created&quot; |



