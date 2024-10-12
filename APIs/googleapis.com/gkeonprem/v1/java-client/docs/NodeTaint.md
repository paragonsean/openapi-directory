

# NodeTaint

NodeTaint applied to every Kubernetes node in a node pool. Kubernetes taints can be used together with tolerations to control how workloads are scheduled to your nodes. Node taints are permanent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effect** | [**EffectEnum**](#EffectEnum) | The taint effect. |  [optional] |
|**key** | **String** | Key associated with the effect. |  [optional] |
|**value** | **String** | Value associated with the effect. |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| EFFECT_UNSPECIFIED | &quot;EFFECT_UNSPECIFIED&quot; |
| NO_SCHEDULE | &quot;NO_SCHEDULE&quot; |
| PREFER_NO_SCHEDULE | &quot;PREFER_NO_SCHEDULE&quot; |
| NO_EXECUTE | &quot;NO_EXECUTE&quot; |



