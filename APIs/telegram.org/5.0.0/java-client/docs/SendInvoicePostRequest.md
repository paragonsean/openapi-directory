

# SendInvoicePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found |  [optional] |
|**chatId** | **Integer** | Unique identifier for the target private chat |  |
|**currency** | **String** | Three-letter ISO 4217 currency code, see [more on currencies](/bots/payments#supported-currencies) |  |
|**description** | **String** | Product description, 1-255 characters |  |
|**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |  [optional] |
|**isFlexible** | **Boolean** | Pass *True*, if the final price depends on the shipping method |  [optional] |
|**needEmail** | **Boolean** | Pass *True*, if you require the user&#39;s email address to complete the order |  [optional] |
|**needName** | **Boolean** | Pass *True*, if you require the user&#39;s full name to complete the order |  [optional] |
|**needPhoneNumber** | **Boolean** | Pass *True*, if you require the user&#39;s phone number to complete the order |  [optional] |
|**needShippingAddress** | **Boolean** | Pass *True*, if you require the user&#39;s shipping address to complete the order |  [optional] |
|**payload** | **String** | Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes. |  |
|**photoHeight** | **Integer** | Photo height |  [optional] |
|**photoSize** | **Integer** | Photo size |  [optional] |
|**photoUrl** | **String** | URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for. |  [optional] |
|**photoWidth** | **Integer** | Photo width |  [optional] |
|**prices** | [**List&lt;LabeledPrice&gt;**](LabeledPrice.md) | Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.) |  |
|**providerData** | **String** | A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider. |  [optional] |
|**providerToken** | **String** | Payments provider token, obtained via [Botfather](https://t.me/botfather) |  |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**replyToMessageId** | **Integer** | If the message is a reply, ID of the original message |  [optional] |
|**sendEmailToProvider** | **Boolean** | Pass *True*, if user&#39;s email address should be sent to provider |  [optional] |
|**sendPhoneNumberToProvider** | **Boolean** | Pass *True*, if user&#39;s phone number should be sent to provider |  [optional] |
|**startParameter** | **String** | Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter |  |
|**title** | **String** | Product name, 1-32 characters |  |



