

# UpdateNetworkAnalyzerConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**traceContent** | [**CreateNetworkAnalyzerConfigurationRequestTraceContent**](CreateNetworkAnalyzerConfigurationRequestTraceContent.md) |  |  [optional] |
|**wirelessDevicesToAdd** | **List&lt;String&gt;** | Wireless device resources to add to the network analyzer configuration. Provide the &lt;code&gt;WirelessDeviceId&lt;/code&gt; of the resource to add in the input array. |  [optional] |
|**wirelessDevicesToRemove** | **List&lt;String&gt;** | Wireless device resources to remove from the network analyzer configuration. Provide the &lt;code&gt;WirelessDeviceId&lt;/code&gt; of the resources to remove in the input array. |  [optional] |
|**wirelessGatewaysToAdd** | **List&lt;String&gt;** | Wireless gateway resources to add to the network analyzer configuration. Provide the &lt;code&gt;WirelessGatewayId&lt;/code&gt; of the resource to add in the input array. |  [optional] |
|**wirelessGatewaysToRemove** | **List&lt;String&gt;** | Wireless gateway resources to remove from the network analyzer configuration. Provide the &lt;code&gt;WirelessGatewayId&lt;/code&gt; of the resources to remove in the input array. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**multicastGroupsToAdd** | **List&lt;String&gt;** | Multicast group resources to add to the network analyzer configuration. Provide the &lt;code&gt;MulticastGroupId&lt;/code&gt; of the resource to add in the input array. |  [optional] |
|**multicastGroupsToRemove** | **List&lt;String&gt;** | Multicast group resources to remove from the network analyzer configuration. Provide the &lt;code&gt;MulticastGroupId&lt;/code&gt; of the resource to remove in the input array. |  [optional] |



