# TelegramBotApi.SendDicePostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found | [optional] 
**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  | 
**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**emoji** | **String** | Emoji on which the dice throw animation is based. Currently, must be one of “&lt;img alt&#x3D;\&quot;🎲\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EB2.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, “&lt;img alt&#x3D;\&quot;🎯\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EAF.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, “&lt;img alt&#x3D;\&quot;🏀\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8F80.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, “&lt;img alt&#x3D;\&quot;⚽\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/E29ABD.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, or “&lt;img alt&#x3D;\&quot;🎰\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EB0.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”. Dice can have values 1-6 for “&lt;img alt&#x3D;\&quot;🎲\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EB2.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;” and “&lt;img alt&#x3D;\&quot;🎯\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EAF.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, values 1-5 for “&lt;img alt&#x3D;\&quot;🏀\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8F80.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;” and “&lt;img alt&#x3D;\&quot;⚽\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/E29ABD.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”, and values 1-64 for “&lt;img alt&#x3D;\&quot;🎰\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EB0.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;”. Defaults to “&lt;img alt&#x3D;\&quot;🎲\&quot; src&#x3D;\&quot;//telegram.org/img/emoji/40/F09F8EB2.png\&quot; height&#x3D;\&quot;20\&quot; width&#x3D;\&quot;20\&quot; /&gt;” | [optional] [default to &#39;🎲&#39;]
**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  | [optional] 
**replyToMessageId** | **Number** | If the message is a reply, ID of the original message | [optional] 



## Enum: EmojiEnum


* `🎲` (value: `"🎲"`)

* `🎯` (value: `"🎯"`)

* `🏀` (value: `"🏀"`)

* `⚽` (value: `"⚽"`)

* `🎰` (value: `"🎰"`)




