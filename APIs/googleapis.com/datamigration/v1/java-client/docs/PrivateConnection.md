

# PrivateConnection

The PrivateConnection resource is used to establish private connectivity with the customer's network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The create time of the resource. |  [optional] [readonly] |
|**displayName** | **String** | The private connection display name. |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. |  [optional] |
|**name** | **String** | The name of the resource. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the private connection. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last update time of the resource. |  [optional] [readonly] |
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
| DELETED | &quot;DELETED&quot; |



