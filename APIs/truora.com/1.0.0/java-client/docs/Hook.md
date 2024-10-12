

# Hook

Represents a hook configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | **List&lt;String&gt;** | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Entity events you want to be notified. If all is selected, there is no need to enter actions |  [optional] |
|**signingKey** | **String** | Secret random hexadecimal key used to sign the event and confirm its legitimacy. Signing keys are used to decode the JWT you get as payload from events |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | indicates whether the hook is active or not. enabled by default |  [optional] |
|**subscriberType** | **String** | Platform with an endpoint ready to process the information. Only web is supported currently |  [optional] |
|**subscriberUrl** | **String** | Link where notification requests will be sent, required when subscriber_type is web |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| CHECK | &quot;check&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



