

# AnswerCallbackQueryPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheTime** | **Integer** | The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0. |  [optional] |
|**callbackQueryId** | **String** | Unique identifier for the query to be answered |  |
|**showAlert** | **Boolean** | If *true*, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to *false*. |  [optional] |
|**text** | **String** | Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters |  [optional] |
|**url** | **String** | URL that will be opened by the user&#39;s client. If you have created a [Game](https://core.telegram.org/bots/api/#game) and accepted the conditions via [@Botfather](https://t.me/botfather), specify the URL that opens your game — note that this will only work if the query comes from a [*callback\\_game*](https://core.telegram.org/bots/api/#inlinekeyboardbutton) button.    Otherwise, you may use links like &#x60;t.me/your_bot?start&#x3D;XXXX&#x60; that open your bot with a parameter. |  [optional] |



