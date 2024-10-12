

# CreateFlowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityZone** | **String** | The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region. |  [optional] |
|**entitlements** | [**List&lt;GrantEntitlementRequest&gt;**](GrantEntitlementRequest.md) | The entitlements that you want to grant on a flow. |  [optional] |
|**mediaStreams** | [**List&lt;AddMediaStreamRequest&gt;**](AddMediaStreamRequest.md) | The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow. |  [optional] |
|**name** | **String** | The name of the flow. |  |
|**outputs** | [**List&lt;AddOutputRequest&gt;**](AddOutputRequest.md) | The outputs that you want to add to this flow. |  [optional] |
|**source** | [**CreateFlowRequestSource**](CreateFlowRequestSource.md) |  |  [optional] |
|**sourceFailoverConfig** | [**CreateBridgeRequestSourceFailoverConfig**](CreateBridgeRequestSourceFailoverConfig.md) |  |  [optional] |
|**sources** | [**List&lt;SetSourceRequest&gt;**](SetSourceRequest.md) |  |  [optional] |
|**vpcInterfaces** | [**List&lt;VpcInterfaceRequest&gt;**](VpcInterfaceRequest.md) | The VPC interfaces you want on the flow. |  [optional] |
|**maintenance** | [**CreateFlowRequestMaintenance**](CreateFlowRequestMaintenance.md) |  |  [optional] |



