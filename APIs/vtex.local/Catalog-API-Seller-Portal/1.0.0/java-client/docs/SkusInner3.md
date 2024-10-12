

# SkusInner3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**Dimensions**](Dimensions.md) |  |  |
|**ean** | **String** | Unique SKU identification code (barcode), composed of up to 13 numeric characters. |  [optional] |
|**externalId** | **String** | Unique reference code created to improve the store&#39;s organization. This is not a required field. |  [optional] |
|**id** | **String** | SKU unique identifier number. Do not include this field when adding a new SKU, only when editing existing SKUs. |  [optional] |
|**images** | **List&lt;Object&gt;** | SKU&#39;s images IDs. |  |
|**isActive** | **Boolean** | Defines if the SKU is active (&#x60;true&#x60;) or inactive (&#x60;false&#x60;). |  |
|**manufacturerCode** | **String** | SKU reference code in the store. |  [optional] |
|**name** | **String** | SKU Name. Use simple words and avoid other languages or complex writing. This field is essential for SEO and must respect the 150 character limit. |  [optional] |
|**specs** | [**List&lt;SpecsInner&gt;**](SpecsInner.md) | SKU specifications. This field is mandatory, but nullable if there is only one SKU. |  |
|**weight** | **Integer** | SKU weight. |  |



