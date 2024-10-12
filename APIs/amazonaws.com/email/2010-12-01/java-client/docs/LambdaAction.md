

# LambdaAction

<p>When included in a receipt rule, this action calls an AWS Lambda function and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).</p> <p>To enable Amazon SES to call your AWS Lambda function or to publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about giving permissions, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html\">Amazon SES Developer Guide</a>.</p> <p>For information about using AWS Lambda actions in receipt rules, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html\">Amazon SES Developer Guide</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topicArn** | [**String**](String.md) |  |  [optional] |
|**functionArn** | [**String**](String.md) |  |  |
|**invocationType** | [**InvocationType**](InvocationType.md) |  |  [optional] |



