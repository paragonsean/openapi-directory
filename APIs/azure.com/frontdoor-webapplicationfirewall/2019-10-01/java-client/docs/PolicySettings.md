

# PolicySettings

Defines top-level WebApplicationFirewallPolicy configuration settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customBlockResponseBody** | **String** | If the action type is block, customer can override the response body. The body must be specified in base64 encoding. |  [optional] |
|**customBlockResponseStatusCode** | **Integer** | If the action type is block, customer can override the response status code. |  [optional] |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Describes if the policy is in enabled or disabled state. Defaults to Enabled if not specified. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Describes if it is in detection mode or prevention mode at policy level. |  [optional] |
|**redirectUrl** | **String** | If action type is redirect, this field represents redirect URL for the client. |  [optional] |



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



