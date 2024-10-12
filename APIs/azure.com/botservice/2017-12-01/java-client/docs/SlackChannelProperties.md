

# SlackChannelProperties

The parameters to provide for the Slack channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The Slack client id |  |
|**clientSecret** | **String** | The Slack client secret. Value only returned through POST to the action Channel List API, otherwise empty. |  |
|**isEnabled** | **Boolean** | Whether this channel is enabled for the bot |  |
|**isValidated** | **Boolean** | Whether this channel is validated for the bot |  [optional] [readonly] |
|**landingPageUrl** | **String** | The Slack landing page Url |  [optional] |
|**lastSubmissionId** | **String** | The Sms auth token |  [optional] [readonly] |
|**redirectAction** | **String** | The Slack redirect action |  [optional] [readonly] |
|**registerBeforeOAuthFlow** | **Boolean** | Whether to register the settings before OAuth validation is performed. Recommended to True. |  [optional] [readonly] |
|**verificationToken** | **String** | The Slack verification token. Value only returned through POST to the action Channel List API, otherwise empty. |  |



