

# CollaborationAllowlistExemptTarget

The user that is exempt from any of the restrictions imposed by the list of allowed collaboration domains for this enterprise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time the entry was created |  [optional] |
|**enterprise** | [**CollaborationAllowlistExemptTargetEnterprise**](CollaborationAllowlistExemptTargetEnterprise.md) |  |  [optional] |
|**id** | **String** | The unique identifier for this exemption |  [optional] |
|**modifiedAt** | **OffsetDateTime** | The time the entry was modified |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;collaboration_whitelist&#x60; |  [optional] |
|**user** | [**CollaborationAllowlistExemptTargetUser**](CollaborationAllowlistExemptTargetUser.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COLLABORATION_WHITELIST | &quot;collaboration_whitelist&quot; |



