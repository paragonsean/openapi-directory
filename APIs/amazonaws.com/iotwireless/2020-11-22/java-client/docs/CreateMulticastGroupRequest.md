

# CreateMulticastGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the multicast group. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. |  [optional] |
|**loRaWAN** | [**CreateMulticastGroupRequestLoRaWAN**](CreateMulticastGroupRequestLoRaWAN.md) |  |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. |  [optional] |



