

# AwsAccessKeys


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKeyId** | **String** | The AWS key ID for the AWS IAM user. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. |  |
|**authenticationMode** | [**AuthenticationModeEnum**](#AuthenticationModeEnum) | Authentication method is using AWS credentials (AWS key ID and secret key). |  [optional] |
|**secretAccessKey** | **String** | The AWS secret key for the AWS IAM user. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/authentication-for-reactor-rules-for-aws-reactor-events-for-lambda-functions-reactor-firehose-for-aws-sqs-and-kinesis\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. |  |



## Enum: AuthenticationModeEnum

| Name | Value |
|---- | -----|
| CREDENTIALS | &quot;credentials&quot; |



