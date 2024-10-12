

# UpdateRoutingProfileAgentAvailabilityTimerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentAvailabilityTimer** | [**AgentAvailabilityTimerEnum**](#AgentAvailabilityTimerEnum) | Whether agents with this routing profile will have their routing order calculated based on &lt;i&gt;time since their last inbound contact&lt;/i&gt; or &lt;i&gt;longest idle time&lt;/i&gt;.  |  |



## Enum: AgentAvailabilityTimerEnum

| Name | Value |
|---- | -----|
| ACTIVITY | &quot;TIME_SINCE_LAST_ACTIVITY&quot; |
| INBOUND | &quot;TIME_SINCE_LAST_INBOUND&quot; |



