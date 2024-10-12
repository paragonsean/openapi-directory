

# SMSSandboxPhoneNumber

<p>A verified or pending destination phone number in the SMS sandbox.</p> <p>When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the <i>SMS sandbox</i>. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see <a href=\"https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\">SMS sandbox</a> in the <i>Amazon SNS Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | [**String**](String.md) |  |  [optional] |
|**status** | [**SMSSandboxPhoneNumberVerificationStatus**](SMSSandboxPhoneNumberVerificationStatus.md) |  |  [optional] |



