# ControlApiV1.AwsKinesisRulePatchTargetAuthentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKeyId** | **String** | The AWS key ID for the AWS IAM user. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. | 
**authenticationMode** | **String** | Authentication method is using the ARN of an assumable role. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. | [optional] 
**secretAccessKey** | **String** | The AWS secret key for the AWS IAM user. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. | 
**assumeRoleArn** | **String** | If you are using the \&quot;ARN of an assumable role\&quot; authentication method, this is your Assume Role ARN. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. | 



## Enum: AuthenticationModeEnum


* `assumeRole` (value: `"assumeRole"`)




