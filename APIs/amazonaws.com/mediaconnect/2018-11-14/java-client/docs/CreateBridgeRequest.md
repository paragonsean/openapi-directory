

# CreateBridgeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**egressGatewayBridge** | [**CreateBridgeRequestEgressGatewayBridge**](CreateBridgeRequestEgressGatewayBridge.md) |  |  [optional] |
|**ingressGatewayBridge** | [**CreateBridgeRequestIngressGatewayBridge**](CreateBridgeRequestIngressGatewayBridge.md) |  |  [optional] |
|**name** | **String** | The name of the bridge. This name can not be modified after the bridge is created. |  |
|**outputs** | [**List&lt;AddBridgeOutputRequest&gt;**](AddBridgeOutputRequest.md) | The outputs that you want to add to this bridge. |  [optional] |
|**placementArn** | **String** | The bridge placement Amazon Resource Number (ARN). |  |
|**sourceFailoverConfig** | [**CreateBridgeRequestSourceFailoverConfig**](CreateBridgeRequestSourceFailoverConfig.md) |  |  [optional] |
|**sources** | [**List&lt;AddBridgeSourceRequest&gt;**](AddBridgeSourceRequest.md) | The sources that you want to add to this bridge. |  |



