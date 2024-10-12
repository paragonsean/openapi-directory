# AwsIoTWireless.UpdateDestinationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressionType** | **String** | The type of value in &lt;code&gt;Expression&lt;/code&gt;. | [optional] 
**expression** | **String** | The new rule name or topic rule to send messages to. | [optional] 
**description** | **String** | The description of the new resource. | [optional] 
**roleArn** | **String** | The ARN of the IAM Role that authorizes the destination. | [optional] 



## Enum: ExpressionTypeEnum


* `RuleName` (value: `"RuleName"`)

* `MqttTopic` (value: `"MqttTopic"`)




