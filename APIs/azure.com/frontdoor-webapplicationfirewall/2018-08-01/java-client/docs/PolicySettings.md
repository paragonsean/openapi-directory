

# PolicySettings

Defines contents of a web application firewall global configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | describes if the policy is in enabled state or disabled state |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Describes if it is in detection mode  or prevention mode at policy level |  [optional] |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| PREVENTION | &quot;Prevention&quot; |
| DETECTION | &quot;Detection&quot; |



