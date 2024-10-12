

# FreeInstanceMetadata

Free instance specific metadata that is kept even after an instance has been upgraded for tracking purposes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expireBehavior** | [**ExpireBehaviorEnum**](#ExpireBehaviorEnum) | Specifies the expiration behavior of a free instance. The default of ExpireBehavior is &#x60;REMOVE_AFTER_GRACE_PERIOD&#x60;. This can be modified during or after creation, and before expiration. |  [optional] |
|**expireTime** | **String** | Output only. Timestamp after which the instance will either be upgraded or scheduled for deletion after a grace period. ExpireBehavior is used to choose between upgrading or scheduling the free instance for deletion. This timestamp is set during the creation of a free instance. |  [optional] [readonly] |
|**upgradeTime** | **String** | Output only. If present, the timestamp at which the free instance was upgraded to a provisioned instance. |  [optional] [readonly] |



## Enum: ExpireBehaviorEnum

| Name | Value |
|---- | -----|
| EXPIRE_BEHAVIOR_UNSPECIFIED | &quot;EXPIRE_BEHAVIOR_UNSPECIFIED&quot; |
| FREE_TO_PROVISIONED | &quot;FREE_TO_PROVISIONED&quot; |
| REMOVE_AFTER_GRACE_PERIOD | &quot;REMOVE_AFTER_GRACE_PERIOD&quot; |



