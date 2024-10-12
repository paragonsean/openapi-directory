

# GoogleCloudApigeeV1NatAddress

Apigee NAT(network address translation) address. A NAT address is a static external IP address used for Internet egress traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | Output only. The static IPV4 address. |  [optional] [readonly] |
|**name** | **String** | Required. Resource ID of the NAT address. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the nat address. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| RESERVED | &quot;RESERVED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |



