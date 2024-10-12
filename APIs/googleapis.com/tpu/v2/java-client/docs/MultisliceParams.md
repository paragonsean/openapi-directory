

# MultisliceParams

Parameters to specify for multislice QueuedResource requests. This message must be populated in case of multislice requests instead of node_id.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeCount** | **Integer** | Required. Number of nodes with this spec. The system will attempt to provison \&quot;node_count\&quot; nodes as part of the request. This needs to be &gt; 1. |  [optional] |
|**nodeIdPrefix** | **String** | Optional. Prefix of node_ids in case of multislice request. Should follow the &#x60;^[A-Za-z0-9_.~+%-]+$&#x60; regex format. If node_count &#x3D; 3 and node_id_prefix &#x3D; \&quot;np\&quot;, node ids of nodes created will be \&quot;np-0\&quot;, \&quot;np-1\&quot;, \&quot;np-2\&quot;. If this field is not provided we use queued_resource_id as the node_id_prefix. |  [optional] |



