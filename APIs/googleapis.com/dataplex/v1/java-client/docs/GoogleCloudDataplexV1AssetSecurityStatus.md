

# GoogleCloudDataplexV1AssetSecurityStatus

Security policy status of the asset. Data security policy, i.e., readers, writers & owners, should be specified in the lake/zone/asset IAM policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Additional information about the current state. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the security policy applied to the attached resource. |  [optional] |
|**updateTime** | **String** | Last update time of the status. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| APPLYING | &quot;APPLYING&quot; |
| ERROR | &quot;ERROR&quot; |



