# ServiceConsumerManagementApi.V1beta1GenerateDefaultIdentityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachStatus** | **String** | Status of the role attachment. Under development (go/si-attach-role), currently always return ATTACH_STATUS_UNSPECIFIED) | [optional] 
**identity** | [**V1beta1DefaultIdentity**](V1beta1DefaultIdentity.md) |  | [optional] 
**role** | **String** | Role attached to consumer project. Empty if not attached in this request. (Under development, currently always return empty.) | [optional] 



## Enum: AttachStatusEnum


* `ATTACH_STATUS_UNSPECIFIED` (value: `"ATTACH_STATUS_UNSPECIFIED"`)

* `ATTACHED` (value: `"ATTACHED"`)

* `ATTACH_SKIPPED` (value: `"ATTACH_SKIPPED"`)

* `PREVIOUSLY_ATTACHED` (value: `"PREVIOUSLY_ATTACHED"`)

* `ATTACH_DENIED_BY_ORG_POLICY` (value: `"ATTACH_DENIED_BY_ORG_POLICY"`)




