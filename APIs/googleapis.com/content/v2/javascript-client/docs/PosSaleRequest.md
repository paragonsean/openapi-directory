# ContentApiForShopping.PosSaleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentLanguage** | **String** | Required. The two-letter ISO 639-1 language code for the item. | [optional] 
**gtin** | **String** | Global Trade Item Number. | [optional] 
**itemId** | **String** | Required. A unique identifier for the item. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**quantity** | **String** | Required. The relative change of the available quantity. Negative for items returned. | [optional] 
**saleId** | **String** | A unique ID to group items from the same sale event. | [optional] 
**storeCode** | **String** | Required. The identifier of the merchant&#39;s store. Either a &#x60;storeCode&#x60; inserted via the API or the code of the store in Google My Business. | [optional] 
**targetCountry** | **String** | Required. The CLDR territory code for the item. | [optional] 
**timestamp** | **String** | Required. The inventory timestamp, in ISO 8601 format. | [optional] 


