

# CacheHealth

An indication of cache health.  Gives more information about health than just that related to provisioning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | List of cache health states. |  [optional] |
|**statusDescription** | **String** | Describes explanation of state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| HEALTHY | &quot;Healthy&quot; |
| DEGRADED | &quot;Degraded&quot; |
| DOWN | &quot;Down&quot; |
| TRANSITIONING | &quot;Transitioning&quot; |
| STOPPING | &quot;Stopping&quot; |
| STOPPED | &quot;Stopped&quot; |
| UPGRADING | &quot;Upgrading&quot; |
| FLUSHING | &quot;Flushing&quot; |



