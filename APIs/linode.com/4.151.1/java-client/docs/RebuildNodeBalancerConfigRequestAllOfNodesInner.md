

# RebuildNodeBalancerConfigRequestAllOfNodesInner

NodeBalancer Node request object including ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The private IP Address where this backend can be reached. This _must_ be a private IP address.  |  [optional] |
|**id** | **Integer** | The unique ID of the Node to update. |  [optional] |
|**label** | **String** | The label for this node.  This is for display purposes only.  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode this NodeBalancer should use when sending traffic to this backend. * If set to &#x60;accept&#x60; this backend is accepting traffic. * If set to &#x60;reject&#x60; this backend will not receive traffic. * If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already   pinned to it will continue to be routed to it.  * If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes   are down.  |  [optional] |
|**weight** | **Integer** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic.  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| REJECT | &quot;reject&quot; |
| DRAIN | &quot;drain&quot; |
| BACKUP | &quot;backup&quot; |



