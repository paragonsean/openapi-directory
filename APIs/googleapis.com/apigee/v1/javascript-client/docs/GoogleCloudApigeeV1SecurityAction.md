# ApigeeApi.GoogleCloudApigeeV1SecurityAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **Object** | Message that should be set in case of an Allow Action. This does not have any fields. | [optional] 
**conditionConfig** | [**GoogleCloudApigeeV1SecurityActionConditionConfig**](GoogleCloudApigeeV1SecurityActionConditionConfig.md) |  | [optional] 
**createTime** | **String** | Output only. The create time for this SecurityAction. | [optional] [readonly] 
**deny** | [**GoogleCloudApigeeV1SecurityActionDeny**](GoogleCloudApigeeV1SecurityActionDeny.md) |  | [optional] 
**description** | **String** | Optional. An optional user provided description of the SecurityAction. | [optional] 
**expireTime** | **String** | The expiration for this SecurityAction. | [optional] 
**flag** | [**GoogleCloudApigeeV1SecurityActionFlag**](GoogleCloudApigeeV1SecurityActionFlag.md) |  | [optional] 
**name** | **String** | Immutable. This field is ignored during creation as per AIP-133. Please set the &#x60;security_action_id&#x60; field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action} | [optional] 
**state** | **String** | Required. Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced. | [optional] 
**ttl** | **String** | Input only. The TTL for this SecurityAction. | [optional] 
**updateTime** | **String** | Output only. The update time for this SecurityAction. This reflects when this SecurityAction changed states. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




