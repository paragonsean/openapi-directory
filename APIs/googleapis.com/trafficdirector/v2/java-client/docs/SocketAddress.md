

# SocketAddress

[#next-free-field: 7]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The address for this socket. :ref:&#x60;Listeners &#x60; will bind to the address. An empty address is not allowed. Specify &#x60;&#x60;0.0.0.0&#x60;&#x60; or &#x60;&#x60;::&#x60;&#x60; to bind to any address. [#comment:TODO(zuercher) reinstate when implemented: It is possible to distinguish a Listener address via the prefix/suffix matching in :ref:&#x60;FilterChainMatch &#x60;.] When used within an upstream :ref:&#x60;BindConfig &#x60;, the address controls the source address of outbound connections. For :ref:&#x60;clusters &#x60;, the cluster type determines whether the address must be an IP (*STATIC* or *EDS* clusters) or a hostname resolved by DNS (*STRICT_DNS* or *LOGICAL_DNS* clusters). Address resolution can be customized via :ref:&#x60;resolver_name &#x60;. |  [optional] |
|**ipv4Compat** | **Boolean** | When binding to an IPv6 address above, this enables &#x60;IPv4 compatibility &#x60;_. Binding to &#x60;&#x60;::&#x60;&#x60; will allow both IPv4 and IPv6 connections, with peer IPv4 addresses mapped into IPv6 space as &#x60;&#x60;::FFFF:&#x60;&#x60;. |  [optional] |
|**namedPort** | **String** | This is only valid if :ref:&#x60;resolver_name &#x60; is specified below and the named resolver is capable of named port resolution. |  [optional] |
|**portValue** | **Integer** |  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) |  |  [optional] |
|**resolverName** | **String** | The name of the custom resolver. This must have been registered with Envoy. If this is empty, a context dependent default applies. If the address is a concrete IP address, no resolution will occur. If address is a hostname this should be set for resolution other than DNS. Specifying a custom resolver with *STRICT_DNS* or *LOGICAL_DNS* will generate an error at runtime. |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;TCP&quot; |
| UDP | &quot;UDP&quot; |



