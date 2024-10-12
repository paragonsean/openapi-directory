

# PatchRetentionRule

Updates to a rule to expire or retain data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**everySeconds** | **Long** | Duration in seconds for how long data will be kept in the database. 0 means infinite. |  [optional] |
|**shardGroupDurationSeconds** | **Long** | Shard duration measured in seconds. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXPIRE | &quot;expire&quot; |



