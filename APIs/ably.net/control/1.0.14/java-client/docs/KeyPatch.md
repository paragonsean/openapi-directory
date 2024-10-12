

# KeyPatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;CapabilitiesEnum&gt;**](#List&lt;CapabilitiesEnum&gt;) | The capabilities that this key has. More information on capabilities can be found in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/core-features/authentication#capabilities-explained\&quot;&gt;Ably documentation&lt;/a&gt;. |  [optional] |
|**channels** | **String** | Specify the channels and queues that this key can be used with. |  [optional] |
|**name** | **String** | The name for your API key. This is a friendly name for your reference. |  [optional] |



## Enum: List&lt;CapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| PUBLISH | &quot;publish&quot; |
| SUBSCRIBE | &quot;subscribe&quot; |
| HISTORY | &quot;history&quot; |
| PRESENCE | &quot;presence&quot; |
| CHANNEL_METADATA | &quot;channel-metadata&quot; |
| PUSH_ADMIN | &quot;push-admin&quot; |
| PUSH_SUBSCRIBE | &quot;push-subscribe&quot; |
| STATISTICS | &quot;statistics&quot; |



