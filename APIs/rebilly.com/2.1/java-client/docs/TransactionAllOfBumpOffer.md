

# TransactionAllOfBumpOffer

Bump offer information. Null if hasBumpOffer is false.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**language** | **String** | The language of the bump offer that was displayed to user (useful for finding any translation problems). |  [optional] |
|**order** | [**Money**](Money.md) | Initial amount and currency. |  [optional] |
|**outcome** | **PurchaseBumpStatus** |  |  [optional] |
|**presentedOffers** | [**List&lt;PurchaseBumpOffer&gt;**](PurchaseBumpOffer.md) | Offers presented to a customer. |  [optional] |
|**selectedOffer** | [**PurchaseBumpOffer**](PurchaseBumpOffer.md) | Offer selected by a customer. Null if bump offer outcome is not &#x60;selected&#x60;. |  [optional] |
|**version** | **String** | The name of the version that was picked (useful for measuring split tests). |  [optional] |



