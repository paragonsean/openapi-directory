

# CardAcquisitionResponse

It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered by the Customer. Content of the Card Acquisition Response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerLanguage** | **String** | Data related to the POI System. |  [optional] |
|**loyaltyAccount** | [**List&lt;LoyaltyAccount&gt;**](LoyaltyAccount.md) |  |  [optional] |
|**poIData** | [**POIData**](POIData.md) |  |  |
|**paymentBrand** | **List&lt;String&gt;** |  |  [optional] |
|**paymentInstrumentData** | [**PaymentInstrumentData**](PaymentInstrumentData.md) |  |  [optional] |
|**response** | [**Response**](Response.md) |  |  |
|**saleData** | [**SaleData**](SaleData.md) |  |  |



