

# ProxyConfiguration

<p>The configuration details for the App Mesh proxy.</p> <p>For tasks that use the EC2 launch type, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html\">Amazon ECS-optimized Linux AMI</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**ProxyConfigurationType**](ProxyConfigurationType.md) |  |  [optional] |
|**containerName** | [**String**](String.md) |  |  |
|**properties** | **Object** | &lt;p&gt;The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IgnoredUID&lt;/code&gt; - (Required) The user ID (UID) of the proxy container as defined by the &lt;code&gt;user&lt;/code&gt; parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If &lt;code&gt;IgnoredGID&lt;/code&gt; is specified, this field can be empty.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IgnoredGID&lt;/code&gt; - (Required) The group ID (GID) of the proxy container as defined by the &lt;code&gt;user&lt;/code&gt; parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If &lt;code&gt;IgnoredUID&lt;/code&gt; is specified, this field can be empty.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AppPorts&lt;/code&gt; - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the &lt;code&gt;ProxyIngressPort&lt;/code&gt; and &lt;code&gt;ProxyEgressPort&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ProxyIngressPort&lt;/code&gt; - (Required) Specifies the port that incoming traffic to the &lt;code&gt;AppPorts&lt;/code&gt; is directed to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ProxyEgressPort&lt;/code&gt; - (Required) Specifies the port that outgoing traffic from the &lt;code&gt;AppPorts&lt;/code&gt; is directed to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EgressIgnoredPorts&lt;/code&gt; - (Required) The egress traffic going to the specified ports is ignored and not redirected to the &lt;code&gt;ProxyEgressPort&lt;/code&gt;. It can be an empty list.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EgressIgnoredIPs&lt;/code&gt; - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the &lt;code&gt;ProxyEgressPort&lt;/code&gt;. It can be an empty list.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



