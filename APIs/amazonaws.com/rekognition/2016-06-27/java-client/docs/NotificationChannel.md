

# NotificationChannel

The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the completion status of a video analysis operation. For more information, see <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/api-video.html\">Calling Amazon Rekognition Video operations</a>. Note that the Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic. For more information, see <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/api-video-roles.html#api-video-roles-all-topics\">Giving access to multiple Amazon SNS topics</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**snSTopicArn** | [**String**](String.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  |



