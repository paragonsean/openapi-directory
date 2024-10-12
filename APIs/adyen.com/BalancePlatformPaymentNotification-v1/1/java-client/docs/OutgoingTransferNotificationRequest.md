

# OutgoingTransferNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**OutgoingTransferNotificationData**](OutgoingTransferNotificationData.md) | Contains details about the event. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;balancePlatform.outgoingTransfer.created&quot; |
| UPDATED | &quot;balancePlatform.outgoingTransfer.updated&quot; |



