

# PacketCaptureFilter

Filter that is applied to packet capture request. Multiple filters can be applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localIPAddress** | **String** | Local IP Address to be filtered on. Notation: \&quot;127.0.0.1\&quot; for single address entry. \&quot;127.0.0.1-127.0.0.255\&quot; for range. \&quot;127.0.0.1;127.0.0.5\&quot;? for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default &#x3D; null. |  [optional] |
|**localPort** | **String** | Local port to be filtered on. Notation: \&quot;80\&quot; for single port entry.\&quot;80-85\&quot; for range. \&quot;80;443;\&quot; for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default &#x3D; null. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol to be filtered on. |  [optional] |
|**remoteIPAddress** | **String** | Local IP Address to be filtered on. Notation: \&quot;127.0.0.1\&quot; for single address entry. \&quot;127.0.0.1-127.0.0.255\&quot; for range. \&quot;127.0.0.1;127.0.0.5;\&quot; for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default &#x3D; null. |  [optional] |
|**remotePort** | **String** | Remote port to be filtered on. Notation: \&quot;80\&quot; for single port entry.\&quot;80-85\&quot; for range. \&quot;80;443;\&quot; for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default &#x3D; null. |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;TCP&quot; |
| UDP | &quot;UDP&quot; |
| ANY | &quot;Any&quot; |



