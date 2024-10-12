# GkeHubApi.IdentityServiceMembershipState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureReason** | **String** | The reason of the failure. | [optional] 
**installedVersion** | **String** | Installed AIS version. This is the AIS version installed on this member. The values makes sense iff state is OK. | [optional] 
**memberConfig** | [**IdentityServiceMembershipSpec**](IdentityServiceMembershipSpec.md) |  | [optional] 
**state** | **String** | Deployment state on this member | [optional] 



## Enum: StateEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `OK` (value: `"OK"`)

* `ERROR` (value: `"ERROR"`)




