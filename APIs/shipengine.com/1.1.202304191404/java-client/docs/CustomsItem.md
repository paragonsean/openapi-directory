

# CustomsItem

The customs declaration for a single item in the shipment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryOfOrigin** | **String** | The two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) where this item originated  |  [optional] |
|**customsItemId** | **String** | A string that uniquely identifies the customs item |  [readonly] |
|**description** | **String** | A description of the item |  [optional] |
|**harmonizedTariffCode** | **String** | The [Harmonized Tariff Code](https://en.wikipedia.org/wiki/Harmonized_System) of this item. |  [optional] |
|**quantity** | **Integer** | The quantity of this item in the shipment. |  [optional] |
|**sku** | **String** | The SKU (Stock Keeping Unit) of the customs item |  [optional] |
|**skuDescription** | **String** | Description of the Custom Item&#39;s SKU |  [optional] |
|**unitOfMeasure** | **String** |  |  [optional] |
|**value** | [**MonetaryValue**](MonetaryValue.md) | The declared customs value of each item |  [optional] |
|**weight** | [**Weight**](Weight.md) | The item weight |  [optional] |



