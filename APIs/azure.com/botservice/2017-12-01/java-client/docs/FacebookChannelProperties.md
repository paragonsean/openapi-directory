

# FacebookChannelProperties

The parameters to provide for the Facebook channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Facebook application id |  |
|**appSecret** | **String** | Facebook application secret. Value only returned through POST to the action Channel List API, otherwise empty. |  |
|**callbackUrl** | **String** | Callback Url |  [optional] [readonly] |
|**isEnabled** | **Boolean** | Whether this channel is enabled for the bot |  |
|**pages** | [**List&lt;FacebookPage&gt;**](FacebookPage.md) | The list of Facebook pages |  [optional] |
|**verifyToken** | **String** | Verify token. Value only returned through POST to the action Channel List API, otherwise empty. |  [optional] [readonly] |



