

# GetOrder200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affiliateId** | **String** | Three letter code identifying the marketplace where the order was placed. |  [optional] |
|**allowCancellation** | **Boolean** | Indicates whether cancelation is allowed for the order. |  [optional] |
|**allowEdition** | **Boolean** | Indicates whether edition is allowed for the order. |  [optional] |
|**approvedBy** | **String** | User that approved the order, in case of manual approval. |  [optional] |
|**authorizedDate** | **String** | Date in which the order was authorized in UTC. |  [optional] |
|**callCenterOperatorData** | **String** |  |  [optional] |
|**cancelReason** | **String** | Reason for cancelation. |  [optional] |
|**cancelledBy** | **String** | User that canceled the order. |  [optional] |
|**changesAttachment** | [**ChangesAttachment**](ChangesAttachment.md) |  |  [optional] |
|**clientProfileData** | [**ClientProfileData**](ClientProfileData.md) |  |  [optional] |
|**commercialConditionData** | **String** |  |  [optional] |
|**creationDate** | **String** | Creation date. |  [optional] |
|**customData** | **String** |  |  [optional] |
|**emailTracked** | **String** | Email tracked. |  [optional] |
|**followUpEmail** | **String** |  |  [optional] |
|**giftRegistryData** | **String** |  |  [optional] |
|**hostname** | **String** |  |  [optional] |
|**invoiceData** | **Object** | Information pertinent to the order&#39;s invoice. |  [optional] |
|**invoicedDate** | **String** | Date in which the order was invoiced in UTC. |  [optional] |
|**isCheckedIn** | **Boolean** | Indicates whether client is checked in. |  [optional] |
|**isCompleted** | **Boolean** |  |  [optional] |
|**items** | [**List&lt;GetOrder200ResponseItemsInner&gt;**](GetOrder200ResponseItemsInner.md) | Information on each item in the order. |  [optional] |
|**lastChange** | **String** | Date of last change. |  [optional] |
|**lastMessage** | **String** |  |  [optional] |
|**marketingData** | **String** |  |  [optional] |
|**marketplace** | [**Marketplace**](Marketplace.md) |  |  [optional] |
|**marketplaceItems** | **List&lt;String&gt;** | Marketplace items. |  [optional] |
|**marketplaceOrderId** | **String** | ID of the order in the marketplace. |  [optional] |
|**marketplaceServicesEndpoint** | **String** | Marketplace endpoint for post purchase communication. |  [optional] |
|**merchantName** | **String** | Merchant name. |  [optional] |
|**openTextField** | **String** |  |  [optional] |
|**orderFormId** | **String** |  |  [optional] |
|**orderGroup** | **String** | Order group. |  [optional] |
|**orderId** | **String** | Order ID. |  [optional] |
|**origin** | **String** | Origin. |  [optional] |
|**packageAttachment** | [**GetOrder200ResponsePackageAttachment**](GetOrder200ResponsePackageAttachment.md) |  |  [optional] |
|**paymentData** | [**PaymentData**](PaymentData.md) |  |  [optional] |
|**ratesAndBenefitsData** | [**RatesAndBenefitsData**](RatesAndBenefitsData.md) |  |  [optional] |
|**roundingError** | **Integer** |  |  [optional] |
|**salesChannel** | **String** | Sales channel. |  [optional] |
|**sellerOrderId** | **String** | Seller order ID. |  [optional] |
|**sellers** | [**List&lt;Seller&gt;**](Seller.md) |  |  [optional] |
|**sequence** | **String** | Sequence number. |  [optional] |
|**shippingData** | [**ShippingData**](ShippingData.md) |  |  [optional] |
|**status** | **String** | Status in the order workflow. |  [optional] |
|**statusDescription** | **String** | &#x60;Deprecated&#x60;. Status description which is displayed on the Admin panel. |  [optional] |
|**storePreferencesData** | [**StorePreferencesData**](StorePreferencesData.md) |  |  [optional] |
|**totals** | [**List&lt;GetOrder200ResponseTotalsInner&gt;**](GetOrder200ResponseTotalsInner.md) | Information on each of the order&#39;s totals. |  [optional] |
|**value** | **Integer** | Value in cents. |  [optional] |



