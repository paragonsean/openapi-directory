

# UpdateNetworkOneToOneNatRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedInbound** | [**List&lt;UpdateNetworkOneToOneNatRulesRequestRulesInnerAllowedInboundInner&gt;**](UpdateNetworkOneToOneNatRulesRequestRulesInnerAllowedInboundInner.md) | The ports this mapping will provide access on, and the remote IPs that will be allowed access to the resource |  [optional] |
|**lanIp** | **String** | The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN |  |
|**name** | **String** | A descriptive name for the rule |  [optional] |
|**publicIp** | **String** | The IP address that will be used to access the internal resource from the WAN |  [optional] |
|**uplink** | [**UplinkEnum**](#UplinkEnum) | The physical WAN interface on which the traffic will arrive (&#39;internet1&#39; or, if available, &#39;internet2&#39;) |  [optional] |



## Enum: UplinkEnum

| Name | Value |
|---- | -----|
| INTERNET1 | &quot;internet1&quot; |
| INTERNET2 | &quot;internet2&quot; |



