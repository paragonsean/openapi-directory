

# AwsAssumeRole


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assumeRoleArn** | **String** | If you are using the \&quot;ARN of an assumable role\&quot; authentication method, this is your Assume Role ARN. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. |  |
|**authenticationMode** | [**AuthenticationModeEnum**](#AuthenticationModeEnum) | Authentication method is using the ARN of an assumable role. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. |  [optional] |



## Enum: AuthenticationModeEnum

| Name | Value |
|---- | -----|
| ASSUME_ROLE | &quot;assumeRole&quot; |



