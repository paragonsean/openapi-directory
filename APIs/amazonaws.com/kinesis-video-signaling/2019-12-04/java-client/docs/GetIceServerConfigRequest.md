

# GetIceServerConfigRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelARN** | **String** | The ARN of the signaling channel to be used for the peer-to-peer connection between configured peers.  |  |
|**clientId** | **String** | Unique identifier for the viewer. Must be unique within the signaling channel. |  [optional] |
|**service** | [**ServiceEnum**](#ServiceEnum) | Specifies the desired service. Currently, &lt;code&gt;TURN&lt;/code&gt; is the only valid value. |  [optional] |
|**username** | **String** | An optional user ID to be associated with the credentials. |  [optional] |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| TURN | &quot;TURN&quot; |



