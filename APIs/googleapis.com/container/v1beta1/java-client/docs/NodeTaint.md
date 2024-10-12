

# NodeTaint

Kubernetes taint is composed of three fields: key, value, and effect. Effect can only be one of three types: NoSchedule, PreferNoSchedule or NoExecute. See [here](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration) for more information, including usage and the valid values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effect** | [**EffectEnum**](#EffectEnum) | Effect for taint. |  [optional] |
|**key** | **String** | Key for taint. |  [optional] |
|**value** | **String** | Value for taint. |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| EFFECT_UNSPECIFIED | &quot;EFFECT_UNSPECIFIED&quot; |
| NO_SCHEDULE | &quot;NO_SCHEDULE&quot; |
| PREFER_NO_SCHEDULE | &quot;PREFER_NO_SCHEDULE&quot; |
| NO_EXECUTE | &quot;NO_EXECUTE&quot; |



