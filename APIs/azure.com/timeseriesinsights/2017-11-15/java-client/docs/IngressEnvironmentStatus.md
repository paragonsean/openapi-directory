

# IngressEnvironmentStatus

An object that represents the status of ingress on an environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | This string represents the state of ingress operations on an environment. It can be \&quot;Disabled\&quot;, \&quot;Ready\&quot;, \&quot;Running\&quot;, \&quot;Paused\&quot; or \&quot;Unknown\&quot; |  [optional] |
|**stateDetails** | [**EnvironmentStateDetails**](EnvironmentStateDetails.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| READY | &quot;Ready&quot; |
| RUNNING | &quot;Running&quot; |
| PAUSED | &quot;Paused&quot; |
| UNKNOWN | &quot;Unknown&quot; |



