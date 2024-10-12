# LinodeApi.NodeBalancerNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The private IP Address where this backend can be reached. This _must_ be a private IP address.  | [optional] 
**configId** | **Number** | The NodeBalancer Config ID that this Node belongs to.  | [optional] [readonly] 
**id** | **Number** | This node&#39;s unique ID. | [optional] [readonly] 
**label** | **String** | The label for this node.  This is for display purposes only.  | [optional] 
**mode** | **String** | The mode this NodeBalancer should use when sending traffic to this backend. * If set to &#x60;accept&#x60; this backend is accepting traffic. * If set to &#x60;reject&#x60; this backend will not receive traffic. * If set to &#x60;drain&#x60; this backend will not receive _new_ traffic, but connections already   pinned to it will continue to be routed to it.  * If set to &#x60;backup&#x60;, this backend will only receive traffic if all &#x60;accept&#x60; nodes   are down.  | [optional] 
**nodebalancerId** | **Number** | The NodeBalancer ID that this Node belongs to.  | [optional] [readonly] 
**status** | **String** | The current status of this node, based on the configured checks of its NodeBalancer Config.  | [optional] [readonly] 
**weight** | **Number** | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic.  | [optional] 



## Enum: ModeEnum


* `accept` (value: `"accept"`)

* `reject` (value: `"reject"`)

* `drain` (value: `"drain"`)

* `backup` (value: `"backup"`)





## Enum: StatusEnum


* `unknown` (value: `"unknown"`)

* `UP` (value: `"UP"`)

* `DOWN` (value: `"DOWN"`)




