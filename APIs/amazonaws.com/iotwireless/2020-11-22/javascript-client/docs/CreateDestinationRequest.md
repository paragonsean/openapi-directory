# AwsIoTWireless.CreateDestinationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the new resource. | 
**expressionType** | **String** | The type of value in &lt;code&gt;Expression&lt;/code&gt;. | 
**expression** | **String** | The rule name or topic rule to send messages to. | 
**description** | **String** | The description of the new resource. | [optional] 
**roleArn** | **String** | The ARN of the IAM Role that authorizes the destination. | 
**tags** | [**[Tag]**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. | [optional] 
**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. | [optional] 



## Enum: ExpressionTypeEnum


* `RuleName` (value: `"RuleName"`)

* `MqttTopic` (value: `"MqttTopic"`)




