

# Bridge

A Bridge is the connection between your datacenter's Instances and the AWS cloud. A bridge can be used to send video from the AWS cloud to your datacenter or from your datacenter to the AWS cloud.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bridgeArn** | [**String**](String.md) |  |  |
|**bridgeMessages** | [**List**](List.md) |  |  [optional] |
|**bridgeState** | [**BridgeState**](BridgeState.md) |  |  |
|**egressGatewayBridge** | [**BridgeEgressGatewayBridge**](BridgeEgressGatewayBridge.md) |  |  [optional] |
|**ingressGatewayBridge** | [**BridgeIngressGatewayBridge**](BridgeIngressGatewayBridge.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  |
|**outputs** | [**List**](List.md) |  |  [optional] |
|**placementArn** | [**String**](String.md) |  |  |
|**sourceFailoverConfig** | [**BridgeSourceFailoverConfig**](BridgeSourceFailoverConfig.md) |  |  [optional] |
|**sources** | [**List**](List.md) |  |  [optional] |



