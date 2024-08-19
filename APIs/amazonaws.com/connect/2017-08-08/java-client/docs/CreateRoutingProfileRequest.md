

# CreateRoutingProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the routing profile. Must not be more than 127 characters. |  |
|**description** | **String** | Description of the routing profile. Must not be more than 250 characters. |  |
|**defaultOutboundQueueId** | **String** | The default outbound queue for the routing profile. |  |
|**queueConfigs** | [**List&lt;RoutingProfileQueueConfig&gt;**](RoutingProfileQueueConfig.md) | &lt;p&gt;The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.&lt;/p&gt; &lt;p&gt;The limit of 10 array members applies to the maximum number of &lt;code&gt;RoutingProfileQueueConfig&lt;/code&gt; objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;Amazon Connect service quotas&lt;/a&gt;. &lt;/p&gt; |  [optional] |
|**mediaConcurrencies** | [**List&lt;MediaConcurrency&gt;**](MediaConcurrency.md) | The channels that agents can handle in the Contact Control Panel (CCP) for this routing profile. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |
|**agentAvailabilityTimer** | [**AgentAvailabilityTimerEnum**](#AgentAvailabilityTimerEnum) | Whether agents with this routing profile will have their routing order calculated based on &lt;i&gt;time since their last inbound contact&lt;/i&gt; or &lt;i&gt;longest idle time&lt;/i&gt;.  |  [optional] |



## Enum: AgentAvailabilityTimerEnum

| Name | Value |
|---- | -----|
| ACTIVITY | &quot;TIME_SINCE_LAST_ACTIVITY&quot; |
| INBOUND | &quot;TIME_SINCE_LAST_INBOUND&quot; |



