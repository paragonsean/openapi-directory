

# CreateWirelessGatewayTaskDefinitionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCreateTasks** | **Boolean** | Whether to automatically create tasks using this task definition for all gateways with the specified current version. If &lt;code&gt;false&lt;/code&gt;, the task must me created by calling &lt;code&gt;CreateWirelessGatewayTask&lt;/code&gt;. |  |
|**name** | **String** | The name of the new resource. |  [optional] |
|**update** | [**CreateWirelessGatewayTaskDefinitionRequestUpdate**](CreateWirelessGatewayTaskDefinitionRequestUpdate.md) |  |  [optional] |
|**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. |  [optional] |



