

# NetworkConfigurationDiagnosticProfile

Parameters to compare with network configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | **String** | Traffic destination. Accepted values are: &#39;*&#39;, IP Address/CIDR, Service Tag. |  |
|**destinationPort** | **String** | Traffic destination port. Accepted values are &#39;*&#39;, port (for example, 3389) and port range (for example, 80-100). |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the traffic. Accepted values are &#39;Inbound&#39; and &#39;Outbound&#39;. |  |
|**protocol** | **String** | Protocol to be verified on. Accepted values are &#39;*&#39;, TCP, UDP. |  |
|**source** | **String** | Traffic source. Accepted values are &#39;*&#39;, IP Address/CIDR, Service Tag. |  |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;Inbound&quot; |
| OUTBOUND | &quot;Outbound&quot; |



