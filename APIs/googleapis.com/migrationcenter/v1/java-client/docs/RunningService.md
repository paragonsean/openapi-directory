

# RunningService

Guest OS running service details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cmdline** | **String** | Service command line. |  [optional] |
|**exePath** | **String** | Service binary path. |  [optional] |
|**pid** | **String** | Service pid. |  [optional] |
|**serviceName** | **String** | Service name. |  [optional] |
|**startMode** | [**StartModeEnum**](#StartModeEnum) | Service start mode (OS-agnostic). |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Service state (OS-agnostic). |  [optional] |



## Enum: StartModeEnum

| Name | Value |
|---- | -----|
| START_MODE_UNSPECIFIED | &quot;START_MODE_UNSPECIFIED&quot; |
| BOOT | &quot;BOOT&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| AUTO | &quot;AUTO&quot; |
| MANUAL | &quot;MANUAL&quot; |
| DISABLED | &quot;DISABLED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |
| STOPPED | &quot;STOPPED&quot; |



