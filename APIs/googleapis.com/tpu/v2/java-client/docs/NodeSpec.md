

# NodeSpec

Details of the TPU node(s) being requested. Users can request either a single node or multiple nodes. NodeSpec provides the specification for node(s) to be created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multisliceParams** | [**MultisliceParams**](MultisliceParams.md) |  |  [optional] |
|**node** | [**Node**](Node.md) |  |  [optional] |
|**nodeId** | **String** | Optional. The unqualified resource name. Should follow the &#x60;^[A-Za-z0-9_.~+%-]+$&#x60; regex format. This is only specified when requesting a single node. In case of multislice requests, multislice_params must be populated instead. |  [optional] |
|**parent** | **String** | Required. The parent resource name. |  [optional] |



