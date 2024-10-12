

# SweepConfigurationNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**SweepConfigurationNotificationData**](SweepConfigurationNotificationData.md) | Contains event details. |  |
|**environment** | **String** | The environment from which the webhook originated.  Possible values: **test**, **live**. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webhook. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;balancePlatform.balanceAccountSweep.created&quot; |
| UPDATED | &quot;balancePlatform.balanceAccountSweep.updated&quot; |
| DELETED | &quot;balancePlatform.balanceAccountSweep.deleted&quot; |



