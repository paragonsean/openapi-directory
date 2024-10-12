# ConversationApi.RecordConversationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**Action**](Action.md) |  | 
**eventMethod** | **String** | The HTTP method used to send event information to event_url. | [optional] [default to &#39;POST&#39;]
**eventUrl** | **[String]** | The webhook endpoint where recording progress events are sent to. | [optional] 
**format** | [**Format**](Format.md) |  | [optional] 
**split** | **String** | Record the sent and received audio in separate channels of a stereo recording | [optional] [default to &#39;conversation&#39;]


