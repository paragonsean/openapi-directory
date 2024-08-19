

# RegisterTaskDefinitionRequestProxyConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**ProxyConfigurationType**](ProxyConfigurationType.md) |  |  [optional] |
|**containerName** | [**String**](String.md) |  |  |
|**properties** | **Object** | &lt;p&gt;The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IgnoredUID&lt;/code&gt; - (Required) The user ID (UID) of the proxy container as defined by the &lt;code&gt;user&lt;/code&gt; parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If &lt;code&gt;IgnoredGID&lt;/code&gt; is specified, this field can be empty.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IgnoredGID&lt;/code&gt; - (Required) The group ID (GID) of the proxy container as defined by the &lt;code&gt;user&lt;/code&gt; parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If &lt;code&gt;IgnoredUID&lt;/code&gt; is specified, this field can be empty.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AppPorts&lt;/code&gt; - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the &lt;code&gt;ProxyIngressPort&lt;/code&gt; and &lt;code&gt;ProxyEgressPort&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ProxyIngressPort&lt;/code&gt; - (Required) Specifies the port that incoming traffic to the &lt;code&gt;AppPorts&lt;/code&gt; is directed to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ProxyEgressPort&lt;/code&gt; - (Required) Specifies the port that outgoing traffic from the &lt;code&gt;AppPorts&lt;/code&gt; is directed to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EgressIgnoredPorts&lt;/code&gt; - (Required) The egress traffic going to the specified ports is ignored and not redirected to the &lt;code&gt;ProxyEgressPort&lt;/code&gt;. It can be an empty list.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EgressIgnoredIPs&lt;/code&gt; - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the &lt;code&gt;ProxyEgressPort&lt;/code&gt;. It can be an empty list.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



