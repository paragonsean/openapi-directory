

# PrivateConnection

The PrivateConnection resource is used to establish private connectivity between Datastream and a customer's network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The create time of the resource. |  [optional] [readonly] |
|**displayName** | **String** | Required. Display name. |  [optional] |
|**error** | [**Error**](Error.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels. |  [optional] |
|**name** | **String** | Output only. The resource&#39;s name. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the Private Connection. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The update time of the resource. |  [optional] [readonly] |
|**vpcPeeringConfig** | [**VpcPeeringConfig**](VpcPeeringConfig.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| CREATED | &quot;CREATED&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |
| FAILED_TO_DELETE | &quot;FAILED_TO_DELETE&quot; |



