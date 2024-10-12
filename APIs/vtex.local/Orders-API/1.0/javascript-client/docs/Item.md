# OrdersApi.Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfo** | [**AdditionalInfo**](AdditionalInfo.md) |  | 
**assemblies** | **[Object]** | Retrieves information about orders item&#39;s customizations. | 
**attachmentOfferings** | [**[ItemAttachmentOfferingsInner]**](ItemAttachmentOfferingsInner.md) | List of attachments details. | 
**attachments** | **[String]** | Array containing information on attachments. | 
**bundleItems** | **[String]** | Information on services sold along with the item&#39;s SKU. For example, a gift package. | 
**callCenterOperator** | **String** | Call center operator responsible for the order. | 
**commission** | **Number** | Commission value registered for the seller. | 
**components** | **[String]** | Item&#39;s components. | 
**costPrice** | **Number** | Item&#39;s cost price. | 
**detailUrl** | **String** | URL slug of the item. | 
**ean** | **String** | EAN of the SKU. | 
**freightCommission** | **Number** | Value of the freight commission. | 
**id** | **String** | Item&#39;s SKU ID, which is a unique numerical identifier. | 
**imageUrl** | **String** | Item&#39;s SKU image URL. | 
**isGift** | **Boolean** | This field is &#x60;true&#x60; when the item is a gift in order context and &#x60;false&#x60; when it is not. | 
**itemAttachment** | [**ItemAttachment**](ItemAttachment.md) |  | 
**listPrice** | **Number** | Item&#39;s list price. | 
**lockId** | **String** | Reservation ID. | 
**manualPrice** | **String** | Item&#39;s manual price. | 
**measurementUnit** | **String** | Item&#39;s measurement unit. | 
**name** | **String** | Item&#39;s name. | 
**offerings** | **[String]** | Item&#39;s offerings, which are services related to the item. For example, guarantee or installation. | 
**params** | **[String]** | Information about params. | 
**parentAssemblyBinding** | **String** | Parent assembly binding. | 
**parentItemIndex** | **String** | Parent item index. | 
**preSaleDate** | **String** | Item&#39;s pre sale date. | 
**price** | **Number** | Item&#39;s price. | 
**priceDefinitions** | [**ItemPriceDefinitions**](ItemPriceDefinitions.md) |  | 
**priceTags** | **[String]** | List of objects with item&#39;s price modifiers. | 
**priceValidUntil** | **String** | Date until when the price is going to be valid if there is a promotion. | 
**productId** | **String** | ID of the Product associated with the item. | 
**quantity** | **Number** | Quantity of items. | 
**refId** | **String** | Product referencial code associated with the item. | 
**rewardValue** | **Number** | Item&#39;s reward value. | 
**seller** | **String** | Seller related to the order. | 
**sellerSku** | **String** | SKU ID from the seller perspective. | 
**sellingPrice** | **Number** | Item&#39;s selling price. | 
**serialNumbers** | **String** | This field identifies the order in the &#x60;handling&#x60; status in the workflow, and it was used for VTEX internal control. | 
**shippingPrice** | **String** | Item&#39;s shipping price. | 
**tax** | **Number** | Item&#39;s tax. | 
**taxCode** | **String** |  Item&#39;s tax code. | 
**uniqueId** | **String** | Unique ID is an alphanumeric sequence that identifies an SKU in a given order. | 
**unitMultiplier** | **Number** | Item&#39;s unit multiplier. | 


