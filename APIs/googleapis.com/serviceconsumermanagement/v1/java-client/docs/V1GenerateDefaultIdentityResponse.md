

# V1GenerateDefaultIdentityResponse

Response message for the `GenerateDefaultIdentity` method. This response message is assigned to the `response` field of the returned Operation when that operation is done.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachStatus** | [**AttachStatusEnum**](#AttachStatusEnum) | Status of the role attachment. Under development (go/si-attach-role), currently always return ATTACH_STATUS_UNSPECIFIED) |  [optional] |
|**identity** | [**V1DefaultIdentity**](V1DefaultIdentity.md) |  |  [optional] |
|**role** | **String** | Role attached to consumer project. Empty if not attached in this request. (Under development, currently always return empty.) |  [optional] |



## Enum: AttachStatusEnum

| Name | Value |
|---- | -----|
| ATTACH_STATUS_UNSPECIFIED | &quot;ATTACH_STATUS_UNSPECIFIED&quot; |
| ATTACHED | &quot;ATTACHED&quot; |
| ATTACH_SKIPPED | &quot;ATTACH_SKIPPED&quot; |
| PREVIOUSLY_ATTACHED | &quot;PREVIOUSLY_ATTACHED&quot; |
| ATTACH_DENIED_BY_ORG_POLICY | &quot;ATTACH_DENIED_BY_ORG_POLICY&quot; |



