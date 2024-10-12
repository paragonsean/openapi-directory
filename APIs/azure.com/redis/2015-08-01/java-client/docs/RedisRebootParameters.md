

# RedisRebootParameters

Specifies which Redis node(s) to reboot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rebootType** | [**RebootTypeEnum**](#RebootTypeEnum) | Which Redis node(s) to reboot. Depending on this value data loss is possible. |  |
|**shardId** | **Integer** | If clustering is enabled, the ID of the shared be rebooted. |  [optional] |



## Enum: RebootTypeEnum

| Name | Value |
|---- | -----|
| PRIMARY_NODE | &quot;PrimaryNode&quot; |
| SECONDARY_NODE | &quot;SecondaryNode&quot; |
| ALL_NODES | &quot;AllNodes&quot; |



