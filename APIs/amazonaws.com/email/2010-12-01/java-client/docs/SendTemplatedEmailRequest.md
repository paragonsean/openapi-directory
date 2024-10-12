

# SendTemplatedEmailRequest

Represents a request to send a templated email using Amazon SES. For more information, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\">Amazon SES Developer Guide</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**String**](String.md) |  |  |
|**destination** | [**SendTemplatedEmailRequestDestination**](SendTemplatedEmailRequestDestination.md) |  |  |
|**replyToAddresses** | [**List**](List.md) |  |  [optional] |
|**returnPath** | [**String**](String.md) |  |  [optional] |
|**sourceArn** | [**String**](String.md) |  |  [optional] |
|**returnPathArn** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**configurationSetName** | [**String**](String.md) |  |  [optional] |
|**template** | [**String**](String.md) |  |  |
|**templateArn** | [**String**](String.md) |  |  [optional] |
|**templateData** | [**String**](String.md) |  |  |



