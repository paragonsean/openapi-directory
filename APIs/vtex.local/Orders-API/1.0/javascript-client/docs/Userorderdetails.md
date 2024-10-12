# OrdersApi.Userorderdetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliateId** | **String** | Corresponds to the three-digit [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) identification code of the seller responsible for the order. | 
**allowCancellation** | **Boolean** | When set as &#x60;true&#x60;, the order can be canceled, and when set as &#x60;false&#x60;, it is no longer possible to cancel the order. | 
**allowEdition** | **Boolean** | When set as &#x60;true&#x60;, the order can be edited, and when set as &#x60;false&#x60;, it is no longer possible to edit the order. | 
**authorizedDate** | **String** | Authorized order date. | 
**callCenterOperatorData** | **String** | Call center operator responsible for the order. | 
**cancelReason** | **String** | Reason for order cancellation. | 
**cancellationData** | [**UserorderdetailsCancellationData**](UserorderdetailsCancellationData.md) |  | 
**changesAttachment** | [**ChangesAttachment**](ChangesAttachment.md) |  | 
**checkedInPickupPointId** | **String** | If the field &#x60;isCheckedIn&#x60; is set as &#x60;true&#x60;, the &#x60;checkedInPickupPointId&#x60; will retrieve the ID of the physical store where the order was made. | 
**clientPreferencesData** | [**UserorderdetailsClientPreferencesData**](UserorderdetailsClientPreferencesData.md) |  | 
**clientProfileData** | [**ClientProfileData**](ClientProfileData.md) |  | 
**commercialConditionData** | **String** | Information about commercial conditions. | 
**creationDate** | **String** | Order&#39;s creation date. | 
**customData** | **String** | Custom information in the order. This field is useful for storing data not included in other fields, for example, a message for a gift or a name to be printed in a shirt. | 
**followUpEmail** | **String** | Email of the store&#39;s employee responsible for managing the order. | 
**giftRegistryData** | **String** | Information about gift list, when it applies. | 
**hostname** | **String** | Account Hostname registered in License Manager. | 
**invoiceData** | **Object** | Information pertinent to the order&#39;s invoice. | 
**invoicedDate** | **String** | Order&#39;s invoice date. | 
**isCheckedIn** | **Boolean** | This field is set &#x60;true&#x60; when the order was made via inStore and &#x60;false&#x60; when it was not. | 
**isCompleted** | **Boolean** | When set as &#x60;true&#x60;, the order&#39;s payment has been settled, and when set as &#x60;false&#x60;, it has not been settled yet. | 
**itemMetadata** | [**UserorderdetailsItemMetadata**](UserorderdetailsItemMetadata.md) |  | 
**items** | [**[Item]**](Item.md) | Information about order&#39;s items. | 
**lastChange** | **String** | Order&#39;s last change date. | 
**lastMessage** | **String** | Last sent transactional message. | 
**marketingData** | [**UserorderdetailsMarketingData**](UserorderdetailsMarketingData.md) |  | 
**marketplace** | [**Marketplace**](Marketplace.md) |  | 
**marketplaceItems** | **[String]** | Marketplace details object. | 
**marketplaceOrderId** | **String** | Marketplace order ID. | 
**marketplaceServicesEndpoint** | **String** | Marketplace services endpoint. | 
**merchantName** | **String** | Name of the merchant. | 
**openTextField** | **String** | Optional field with order&#39;s additional information. This field must be filled in using the following format:   &#x60;&#x60;&#x60;  {      \&quot;fieldExample\&quot;: \&quot;ValueExample\&quot;    }  &#x60;&#x60;&#x60;   | 
**orderFormId** | **String** | [Order form](https://developers.vtex.com/docs/guides/orderform-fields) ID.  | 
**orderGroup** | **String** | Order&#39;s group ID. | 
**orderId** | **String** | Order ID is a unique code that identifies an order. | 
**origin** | **String** | Order Origin, if &#x60;Marketplace&#x60; or &#x60;Fulfillment&#x60;. | 
**packageAttachment** | [**PackageAttachment**](PackageAttachment.md) |  | 
**paymentData** | [**PaymentData**](PaymentData.md) |  | 
**ratesAndBenefitsData** | [**RatesAndBenefitsData**](RatesAndBenefitsData.md) |  | 
**roundingError** | **Number** | Rounding error total amount, if it applies. For example, in orders with a discount over non-integer multiplier items, the rounding price is performed per item, not after the sum of all items. That can cause a difference in the total discount amount, which is informed in this field. | 
**salesChannel** | **String** | Sales channel (or [trade policy](https://help.vtex.com/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) ID related to the order. | 
**sellerOrderId** | **String** | ID of the seller related to the order. It can be a VTEX seller or an external seller. | 
**sellers** | [**[Seller]**](Seller.md) | List of all sellers associated with the order. | 
**sequence** | **String** | Sequence is a six-digit string that follows the order ID. For example, in order &#x60;1268540501456-01 (501456)&#x60;, the sequence is &#x60;501456&#x60;. | 
**shippingData** | [**ShippingData**](ShippingData.md) |  | 
**status** | **String** | Order [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). | 
**statusDescription** | **String** | &#x60;Deprecated&#x60;. Status description which is displayed on the Admin panel. This field is obsolete and may not return any value. | 
**storePreferencesData** | [**StorePreferencesData**](StorePreferencesData.md) |  | 
**subscriptionData** | [**UserorderdetailsSubscriptionData**](UserorderdetailsSubscriptionData.md) |  | 
**taxData** | [**UserorderdetailsTaxData**](UserorderdetailsTaxData.md) |  | 
**totals** | [**[Total]**](Total.md) | List with details about orders&#39; totals. | 
**value** | **Number** | Order&#39;s total amount. | 


