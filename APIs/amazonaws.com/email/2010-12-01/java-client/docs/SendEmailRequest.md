

# SendEmailRequest

Represents a request to send a single formatted email using Amazon SES. For more information, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-formatted.html\">Amazon SES Developer Guide</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**String**](String.md) |  |  |
|**destination** | [**SendEmailRequestDestination**](SendEmailRequestDestination.md) |  |  |
|**message** | [**SendEmailRequestMessage**](SendEmailRequestMessage.md) |  |  |
|**replyToAddresses** | [**List**](List.md) |  |  [optional] |
|**returnPath** | [**String**](String.md) |  |  [optional] |
|**sourceArn** | [**String**](String.md) |  |  [optional] |
|**returnPathArn** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**configurationSetName** | [**String**](String.md) |  |  [optional] |



