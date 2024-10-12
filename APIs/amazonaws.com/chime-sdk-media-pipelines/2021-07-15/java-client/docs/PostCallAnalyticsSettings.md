

# PostCallAnalyticsSettings

<p>Allows you to specify additional settings for your Call Analytics post-call request, including output locations for your redacted transcript, which IAM role to use, and which encryption key to use.</p> <p> <code>DataAccessRoleArn</code> and <code>OutputLocation</code> are required fields.</p> <p> <code>PostCallAnalyticsSettings</code> provides the same insights as a Call Analytics post-call transcription. For more information, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html\">Post-call analytics with real-time transcriptions</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputLocation** | [**String**](String.md) |  |  |
|**dataAccessRoleArn** | [**String**](String.md) |  |  |
|**contentRedactionOutput** | [**ContentRedactionOutput**](ContentRedactionOutput.md) |  |  [optional] |
|**outputEncryptionKMSKeyId** | [**String**](String.md) |  |  [optional] |



