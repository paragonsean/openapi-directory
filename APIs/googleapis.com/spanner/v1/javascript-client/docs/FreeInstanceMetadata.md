# CloudSpannerApi.FreeInstanceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expireBehavior** | **String** | Specifies the expiration behavior of a free instance. The default of ExpireBehavior is &#x60;REMOVE_AFTER_GRACE_PERIOD&#x60;. This can be modified during or after creation, and before expiration. | [optional] 
**expireTime** | **String** | Output only. Timestamp after which the instance will either be upgraded or scheduled for deletion after a grace period. ExpireBehavior is used to choose between upgrading or scheduling the free instance for deletion. This timestamp is set during the creation of a free instance. | [optional] [readonly] 
**upgradeTime** | **String** | Output only. If present, the timestamp at which the free instance was upgraded to a provisioned instance. | [optional] [readonly] 



## Enum: ExpireBehaviorEnum


* `EXPIRE_BEHAVIOR_UNSPECIFIED` (value: `"EXPIRE_BEHAVIOR_UNSPECIFIED"`)

* `FREE_TO_PROVISIONED` (value: `"FREE_TO_PROVISIONED"`)

* `REMOVE_AFTER_GRACE_PERIOD` (value: `"REMOVE_AFTER_GRACE_PERIOD"`)




