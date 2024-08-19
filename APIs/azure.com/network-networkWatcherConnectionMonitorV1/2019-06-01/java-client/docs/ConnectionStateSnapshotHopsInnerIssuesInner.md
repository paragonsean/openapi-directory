

# ConnectionStateSnapshotHopsInnerIssuesInner

Information about an issue encountered in the process of checking for connectivity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | **List&lt;Map&lt;String, String&gt;&gt;** | Provides additional context on the issue. |  [optional] [readonly] |
|**origin** | [**OriginEnum**](#OriginEnum) | The origin of the issue. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of the issue. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of issue. |  [optional] [readonly] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;Local&quot; |
| INBOUND | &quot;Inbound&quot; |
| OUTBOUND | &quot;Outbound&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;Error&quot; |
| WARNING | &quot;Warning&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| AGENT_STOPPED | &quot;AgentStopped&quot; |
| GUEST_FIREWALL | &quot;GuestFirewall&quot; |
| DNS_RESOLUTION | &quot;DnsResolution&quot; |
| SOCKET_BIND | &quot;SocketBind&quot; |
| NETWORK_SECURITY_RULE | &quot;NetworkSecurityRule&quot; |
| USER_DEFINED_ROUTE | &quot;UserDefinedRoute&quot; |
| PORT_THROTTLED | &quot;PortThrottled&quot; |
| PLATFORM | &quot;Platform&quot; |



