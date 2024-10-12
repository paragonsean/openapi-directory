

# Product

A Product is an item in the company's inventory, and includes information about the price and quantity of all products, and variants thereof, available for sale.  Explore our [data coverage](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-products) for this data type. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | A unique, persistent identifier for this record |  |
|**categorization** | **String** | Retail category that the product is assigned to |  [optional] |
|**description** | **String** | Description of the product recorded in the commerce or point of sale platform. |  [optional] |
|**isGiftCard** | **Boolean** | Whether the product represents a gift card or voucher that can be redeemed in the commerce or POS platform  |  [optional] |
|**name** | **String** | Name of the product in the commerce or POS system |  [optional] |
|**variants** | [**List&lt;ProductVariant&gt;**](ProductVariant.md) |  |  [optional] |



