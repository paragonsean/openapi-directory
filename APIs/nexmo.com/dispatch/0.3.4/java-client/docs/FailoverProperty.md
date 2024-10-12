

# FailoverProperty

Please note that last message does not have failover attribute inside it. All other messages must contain a failover attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditionStatus** | [**ConditionStatusEnum**](#ConditionStatusEnum) | Set the status the message must reach in the expiry_time before failing over. Options are delivered or read. |  [optional] |
|**expiryTime** | **Integer** | In seconds. Minimum value is 15 and maximum value is 86,400 seconds (1 day). |  [optional] |



## Enum: ConditionStatusEnum

| Name | Value |
|---- | -----|
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |



