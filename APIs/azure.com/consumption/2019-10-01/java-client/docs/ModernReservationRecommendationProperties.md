

# ModernReservationRecommendationProperties

The properties of the reservation recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costWithNoReservedInstances** | [**Amount**](Amount.md) |  |  [optional] |
|**firstUsageDate** | **OffsetDateTime** | The usage date for looking back. |  [optional] [readonly] |
|**instanceFlexibilityGroup** | **String** | The instance Flexibility Group. |  [optional] [readonly] |
|**instanceFlexibilityRatio** | **Integer** | The instance Flexibility Ratio. |  [optional] [readonly] |
|**lookBackPeriod** | **String** | The number of days of usage to look back for recommendation. |  [optional] [readonly] |
|**meterId** | **UUID** | The meter id (GUID) |  [optional] [readonly] |
|**netSavings** | [**Amount**](Amount.md) |  |  [optional] |
|**normalizedSize** | **String** | The normalized Size. |  [optional] [readonly] |
|**recommendedQuantity** | **BigDecimal** | Recommended quality for reserved instances. |  [optional] [readonly] |
|**recommendedQuantityNormalized** | **BigDecimal** | The recommended Quantity Normalized. |  [optional] [readonly] |
|**scope** | **String** | Shared or single recommendation. |  [optional] [readonly] |
|**skuProperties** | [**List&lt;SkuProperty&gt;**](SkuProperty.md) | List of sku properties |  [optional] [readonly] |
|**term** | **String** | RI recommendations in one or three year terms. |  [optional] [readonly] |
|**totalCostWithReservedInstances** | [**Amount**](Amount.md) |  |  [optional] |



