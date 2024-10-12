

# IdentityServiceMembershipState

**Anthos Identity Service**: State for a single Membership.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureReason** | **String** | The reason of the failure. |  [optional] |
|**installedVersion** | **String** | Installed AIS version. This is the AIS version installed on this member. The values makes sense iff state is OK. |  [optional] |
|**memberConfig** | [**IdentityServiceMembershipSpec**](IdentityServiceMembershipSpec.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Deployment state on this member |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| OK | &quot;OK&quot; |
| ERROR | &quot;ERROR&quot; |



