

# CreateRoomRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loggingConfigurationIdentifiers** | **List&lt;String&gt;** | Array of logging-configuration identifiers attached to the room. |  [optional] |
|**maximumMessageLength** | **Integer** | Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500. |  [optional] |
|**maximumMessageRatePerSecond** | **Integer** | Maximum number of messages per second that can be sent to the room (by all clients). Default: 10.  |  [optional] |
|**messageReviewHandler** | [**CreateRoomRequestMessageReviewHandler**](CreateRoomRequestMessageReviewHandler.md) |  |  [optional] |
|**name** | **String** | Room name. The value does not need to be unique. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags to attach to the resource. Array of maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for details, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no constraints beyond what is documented there. |  [optional] |



