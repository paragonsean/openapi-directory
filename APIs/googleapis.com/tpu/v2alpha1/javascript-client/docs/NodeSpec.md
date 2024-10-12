# CloudTpuApi.NodeSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiNodeParams** | [**MultiNodeParams**](MultiNodeParams.md) |  | [optional] 
**node** | [**Node**](Node.md) |  | [optional] 
**nodeId** | **String** | The unqualified resource name. Should follow the &#x60;^[A-Za-z0-9_.~+%-]+$&#x60; regex format. This is only specified when requesting a single node. In case of multi-node requests, multi_node_params must be populated instead. It&#39;s an error to specify both node_id and multi_node_params. | [optional] 
**parent** | **String** | Required. The parent resource name. | [optional] 


