

# SendRawEmailRequest

Represents a request to send a single raw email using Amazon SES. For more information, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html\">Amazon SES Developer Guide</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**String**](String.md) |  |  [optional] |
|**destinations** | [**List**](List.md) |  |  [optional] |
|**rawMessage** | [**SendRawEmailRequestRawMessage**](SendRawEmailRequestRawMessage.md) |  |  |
|**fromArn** | [**String**](String.md) |  |  [optional] |
|**sourceArn** | [**String**](String.md) |  |  [optional] |
|**returnPathArn** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**configurationSetName** | [**String**](String.md) |  |  [optional] |



