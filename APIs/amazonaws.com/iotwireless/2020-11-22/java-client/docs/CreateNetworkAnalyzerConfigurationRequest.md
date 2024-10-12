

# CreateNetworkAnalyzerConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the network analyzer configuration. |  |
|**traceContent** | [**CreateNetworkAnalyzerConfigurationRequestTraceContent**](CreateNetworkAnalyzerConfigurationRequestTraceContent.md) |  |  [optional] |
|**wirelessDevices** | **List&lt;String&gt;** | Wireless device resources to add to the network analyzer configuration. Provide the &lt;code&gt;WirelessDeviceId&lt;/code&gt; of the resource to add in the input array. |  [optional] |
|**wirelessGateways** | **List&lt;String&gt;** | Wireless gateway resources to add to the network analyzer configuration. Provide the &lt;code&gt;WirelessGatewayId&lt;/code&gt; of the resource to add in the input array. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. |  [optional] |
|**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. |  [optional] |
|**multicastGroups** | **List&lt;String&gt;** | Multicast Group resources to add to the network analyzer configruation. Provide the &lt;code&gt;MulticastGroupId&lt;/code&gt; of the resource to add in the input array. |  [optional] |



