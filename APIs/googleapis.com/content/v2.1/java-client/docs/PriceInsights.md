

# PriceInsights

Price insights fields requested by the merchant in the query. Field values are only set if the merchant queries `PriceInsightsProductView`. https://support.google.com/merchants/answer/11916926

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictedClicksChangeFraction** | **Double** | The predicted change in clicks as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in clicks. |  [optional] |
|**predictedConversionsChangeFraction** | **Double** | The predicted change in conversions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in conversions). |  [optional] |
|**predictedGrossProfitChangeFraction** | **Double** | *Deprecated*: This field is no longer supported and will start returning 0. The predicted change in gross profit as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in gross profit. |  [optional] |
|**predictedImpressionsChangeFraction** | **Double** | The predicted change in impressions as a fraction after introducing the suggested price compared to current active price. For example, 0.05 is a 5% predicted increase in impressions. |  [optional] |
|**predictedMonthlyGrossProfitChangeCurrencyCode** | **String** | *Deprecated*: This field is no longer supported and will start returning USD for all requests. The predicted monthly gross profit change currency (ISO 4217 code). |  [optional] |
|**predictedMonthlyGrossProfitChangeMicros** | **String** | *Deprecated*: This field is no longer supported and will start returning 0. The predicted change in gross profit in micros (1 millionth of a standard unit, 1 USD &#x3D; 1000000 micros) after introducing the suggested price for a month compared to current active price. |  [optional] |
|**suggestedPriceCurrencyCode** | **String** | The suggested price currency (ISO 4217 code). |  [optional] |
|**suggestedPriceMicros** | **String** | The latest suggested price in micros (1 millionth of a standard unit, 1 USD &#x3D; 1000000 micros) for the product. |  [optional] |



