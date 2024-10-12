

# PaymentInstrumentData

Sent in the result of the payment transaction. For a card, it could also be sent in the CardAcquisition response, to be processed by the Sale System. Data related to the instrument of payment for the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardData** | [**CardData**](CardData.md) |  |  [optional] |
|**checkData** | [**CheckData**](CheckData.md) |  |  [optional] |
|**mobileData** | [**MobileData**](MobileData.md) |  |  [optional] |
|**paymentInstrumentType** | **PaymentInstrumentType** |  |  |
|**protectedCardData** | **String** |  |  [optional] |
|**storedValueAccountID** | [**StoredValueAccountID**](StoredValueAccountID.md) |  |  [optional] |



