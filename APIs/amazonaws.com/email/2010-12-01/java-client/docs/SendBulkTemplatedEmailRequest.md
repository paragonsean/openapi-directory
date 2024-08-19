

# SendBulkTemplatedEmailRequest

Represents a request to send a templated email to multiple destinations using Amazon SES. For more information, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\">Amazon SES Developer Guide</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**String**](String.md) |  |  |
|**sourceArn** | [**String**](String.md) |  |  [optional] |
|**replyToAddresses** | [**List**](List.md) |  |  [optional] |
|**returnPath** | [**String**](String.md) |  |  [optional] |
|**returnPathArn** | [**String**](String.md) |  |  [optional] |
|**configurationSetName** | [**String**](String.md) |  |  [optional] |
|**defaultTags** | [**List**](List.md) |  |  [optional] |
|**template** | [**String**](String.md) |  |  |
|**templateArn** | [**String**](String.md) |  |  [optional] |
|**defaultTemplateData** | [**String**](String.md) |  |  [optional] |
|**destinations** | [**List**](List.md) |  |  |



