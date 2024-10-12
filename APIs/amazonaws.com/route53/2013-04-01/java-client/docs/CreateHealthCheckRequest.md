

# CreateHealthCheckRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerReference** | **String** | &lt;p&gt;A unique string that identifies the request and that allows you to retry a failed &lt;code&gt;CreateHealthCheck&lt;/code&gt; request without the risk of creating two identical health checks:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you send a &lt;code&gt;CreateHealthCheck&lt;/code&gt; request with the same &lt;code&gt;CallerReference&lt;/code&gt; and settings as a previous request, and if the health check doesn&#39;t exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the settings for the existing health check.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you send a &lt;code&gt;CreateHealthCheck&lt;/code&gt; request with the same &lt;code&gt;CallerReference&lt;/code&gt; as a deleted health check, regardless of the settings, Route 53 returns a &lt;code&gt;HealthCheckAlreadyExists&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you send a &lt;code&gt;CreateHealthCheck&lt;/code&gt; request with the same &lt;code&gt;CallerReference&lt;/code&gt; as an existing health check but with different settings, Route 53 returns a &lt;code&gt;HealthCheckAlreadyExists&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you send a &lt;code&gt;CreateHealthCheck&lt;/code&gt; request with a unique &lt;code&gt;CallerReference&lt;/code&gt; but settings identical to an existing health check, Route 53 creates the health check.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**healthCheckConfig** | [**CreateHealthCheckRequestHealthCheckConfig**](CreateHealthCheckRequestHealthCheckConfig.md) |  |  |



