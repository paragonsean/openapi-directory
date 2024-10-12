

# TransportTelegramPatch

The TransportTelegram resource is a collection of transports that carry dispatched alerts to the external Telegram service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**telegramChatId** | **String** | The chat ID for the Telegram service. |  |
|**telegramToken** | **String** | The token for the Telegram service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



