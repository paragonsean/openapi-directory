# TelegramBotApi.Update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackQuery** | [**CallbackQuery**](CallbackQuery.md) |  | [optional] 
**channelPost** | [**Message**](Message.md) |  | [optional] 
**chosenInlineResult** | [**ChosenInlineResult**](ChosenInlineResult.md) |  | [optional] 
**editedChannelPost** | [**Message**](Message.md) |  | [optional] 
**editedMessage** | [**Message**](Message.md) |  | [optional] 
**inlineQuery** | [**InlineQuery**](InlineQuery.md) |  | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**pollAnswer** | [**PollAnswer**](PollAnswer.md) |  | [optional] 
**preCheckoutQuery** | [**PreCheckoutQuery**](PreCheckoutQuery.md) |  | [optional] 
**shippingQuery** | [**ShippingQuery**](ShippingQuery.md) |  | [optional] 
**updateId** | **Number** | The update&#39;s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you&#39;re using [Webhooks](https://core.telegram.org/bots/api/#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially. | 


