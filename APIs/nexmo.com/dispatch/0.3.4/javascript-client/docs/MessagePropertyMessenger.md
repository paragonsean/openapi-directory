# DispatchApi.MessagePropertyMessenger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The use of different category tags enables the business to send messages for different use cases. For Facebook Messenger they need to comply with their [Messaging Types policy]( https://developers.facebook.com/docs/messenger-platform/send-messages#messaging_types). Vonage maps our &#x60;category&#x60; to their &#x60;messaging_type&#x60;. If &#x60;message_tag&#x60; is used, then an additional &#x60;tag&#x60; for that type is mandatory. By default Vonage sends the &#x60;response&#x60; category to Facebook Messenger. | [optional] 
**tag** | **String** | ‘A full list of the possible tags is available on [developers.facebook.com](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)&#39; | [optional] 



## Enum: CategoryEnum


* `response` (value: `"response"`)

* `update` (value: `"update"`)

* `message_tag` (value: `"message_tag"`)




