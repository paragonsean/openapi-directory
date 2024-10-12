

# NodeBalancerNode

A NodeBalancerNode represents a single backend serving requests for a single port of a NodeBalancer.  Nodes are specific to NodeBalancer Configs, and serve traffic over their private IP.  If the same Linode is serving traffic for more than one port on the same NodeBalancer, one NodeBalancer Node is required for each config (port) it should serve requests on.  For example, if you have four backends, and each should response to both HTTP and HTTPS requests, you will need two NodeBalancerConfigs (port 80 and port 443) and four backends each - one for each of the Linodes serving requests for that port. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The private IP Address where this backend can be reached. This _must_ be a private IP address.  |  [optional] |
|**configId** | **Integer** | The NodeBalancer Config ID that this Node belongs to.  |  [optional] [readonly] |
|**id** | **Integer** | This node&#39;s unique ID. |  [optional] [readonly] |
|**label** | **String** | The label for this node.  This is for display purposes only.  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode this NodeBalancer should use when sending traffic to this backend. * If set to &#x60;accept&#x60; this backend is accepting traffic. * If set to &#x60;reject&#x60; this backend will not receive traffic. * If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already   pinned to it will continue to be routed to it.  * If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes   are down.  |  [optional] |
|**nodebalancerId** | **Integer** | The NodeBalancer ID that this Node belongs to.  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of this node, based on the configured checks of its NodeBalancer Config.  |  [optional] [readonly] |
|**weight** | **Integer** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic.  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| REJECT | &quot;reject&quot; |
| DRAIN | &quot;drain&quot; |
| BACKUP | &quot;backup&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| UP | &quot;UP&quot; |
| DOWN | &quot;DOWN&quot; |



