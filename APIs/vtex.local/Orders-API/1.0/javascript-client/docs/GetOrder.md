# OrdersApi.GetOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliateId** | **String** |  | 
**allowCancellation** | **Boolean** |  | 
**allowEdition** | **Boolean** |  | 
**approvedBy** | **String** |  | 
**authorizedDate** | **String** |  | 
**callCenterOperatorData** | **String** |  | 
**cancelReason** | **String** | Explanation for cancellation | 
**cancelledBy** | **String** | User that canceled the order. | 
**changesAttachment** | [**ChangesAttachment**](ChangesAttachment.md) |  | 
**clientProfileData** | [**ClientProfileData**](ClientProfileData.md) |  | 
**commercialConditionData** | **String** |  | 
**creationDate** | **String** |  | 
**customData** | **String** |  | 
**emailTracked** | **String** |  | 
**followUpEmail** | **String** |  | 
**giftRegistryData** | **String** |  | 
**hostname** | **String** |  | 
**invoiceData** | **Object** | Information pertinent to the order&#39;s invoice. | 
**invoicedDate** | **String** |  | 
**isCheckedIn** | **Boolean** |  | 
**isCompleted** | **Boolean** |  | 
**items** | [**[Item]**](Item.md) |  | 
**lastChange** | **String** |  | 
**lastMessage** | **String** |  | 
**marketingData** | **String** |  | 
**marketplace** | [**Marketplace**](Marketplace.md) |  | 
**marketplaceItems** | **[String]** |  | 
**marketplaceOrderId** | **String** |  | 
**marketplaceServicesEndpoint** | **String** |  | 
**merchantName** | **String** |  | 
**openTextField** | **String** | This field must be filled in using the following format:   &#x60;&#x60;&#x60;  {      \&quot;fieldExample\&quot;: \&quot;ValueExample\&quot;    }  &#x60;&#x60;&#x60;   | 
**orderFormId** | **String** |  | 
**orderGroup** | **String** |  | 
**orderId** | **String** |  | 
**origin** | **String** |  | 
**packageAttachment** | [**PackageAttachment**](PackageAttachment.md) |  | 
**paymentData** | [**PaymentData**](PaymentData.md) |  | 
**ratesAndBenefitsData** | [**RatesAndBenefitsData**](RatesAndBenefitsData.md) |  | 
**roundingError** | **Number** |  | 
**salesChannel** | **String** |  | 
**sellerOrderId** | **String** |  | 
**sellers** | [**[Seller]**](Seller.md) |  | 
**sequence** | **String** |  | 
**shippingData** | [**ShippingData**](ShippingData.md) |  | 
**status** | **String** |  | 
**statusDescription** | **String** | &#x60;Deprecated&#x60;. Status description which is displayed on the Admin panel. This field is obsolete and may not return any value. | 
**storePreferencesData** | [**StorePreferencesData**](StorePreferencesData.md) |  | 
**totals** | [**[Total]**](Total.md) |  | 
**value** | **Number** |  | 


