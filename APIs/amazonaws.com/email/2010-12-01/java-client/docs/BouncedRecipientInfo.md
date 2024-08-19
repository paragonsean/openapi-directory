

# BouncedRecipientInfo

<p>Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.</p> <p>For information about receiving email through Amazon SES, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html\">Amazon SES Developer Guide</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recipient** | [**String**](String.md) |  |  |
|**recipientArn** | [**String**](String.md) |  |  [optional] |
|**bounceType** | [**BounceType**](BounceType.md) |  |  [optional] |
|**recipientDsnFields** | [**BouncedRecipientInfoRecipientDsnFields**](BouncedRecipientInfoRecipientDsnFields.md) |  |  [optional] |



