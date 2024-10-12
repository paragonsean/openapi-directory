

# HotelProductPriceVariation

Some prices may vary during a stay, thus here you can see the daily price per period of the stay

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**base** | **String** |  |  [optional] |
|**currency** | **String** | currency Code apply to all elements of the price |  [optional] |
|**endDate** | **LocalDate** | End date of the period Format: YYYY-MM-DD |  |
|**markups** | [**List&lt;Markup&gt;**](Markup.md) |  |  [optional] |
|**sellingTotal** | **String** | sellingTotal &#x3D; Total + margins + markup + totalFees - discounts |  [optional] |
|**startDate** | **LocalDate** | Begin date of the period Format: YYYY-MM-DD |  |
|**total** | **String** | total &#x3D; base + totalTaxes |  [optional] |



