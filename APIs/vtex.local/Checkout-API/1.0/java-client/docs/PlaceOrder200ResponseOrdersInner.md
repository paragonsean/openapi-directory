

# PlaceOrder200ResponseOrdersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowCancelation** | **Boolean** | Indicates whether cancelation is allowed. |  [optional] |
|**allowChangeSeller** | **Boolean** | Indicates whether seller changing is allowed. |  [optional] |
|**allowEdition** | **Boolean** | Indicates whether edition is allowed. |  [optional] |
|**checkedInPickupPointId** | **String** | Checked in pickuppoint. |  [optional] |
|**clientProfileData** | [**AddCoupons200ResponseClientProfileData**](AddCoupons200ResponseClientProfileData.md) |  |  [optional] |
|**creationDate** | **String** | Creation date. |  [optional] |
|**followUpEmail** | **String** | Follow up email address. |  [optional] |
|**hostName** | **String** | Host name. |  [optional] |
|**isCheckedIn** | **Boolean** | Indicates whether order is checked in. |  [optional] |
|**isCompleted** | **Boolean** | Indicates whether order is completed. |  [optional] |
|**isUserDataVisible** | **Boolean** | Indicates whether user data is visible. |  [optional] |
|**itemMetadata** | [**AddCoupons200ResponseItemMetadata**](AddCoupons200ResponseItemMetadata.md) |  |  [optional] |
|**items** | [**List&lt;PlaceOrder200ResponseOrdersInnerItemsInner&gt;**](PlaceOrder200ResponseOrdersInnerItemsInner.md) | Information on each item in the order. |  [optional] |
|**lastChange** | **String** | Last change. |  [optional] |
|**merchantName** | **String** | Merchant name. |  [optional] |
|**orderFormCreationDate** | **String** | &#x60;orderForm&#x60; creation date. |  [optional] |
|**orderGroup** | **String** | Order group. Orders that involve different sellers are split into different orders of a same order group. |  [optional] |
|**orderId** | **String** | ID of the order in the Order Management System (OMS). |  [optional] |
|**paymentData** | [**AddCoupons200ResponsePaymentData**](AddCoupons200ResponsePaymentData.md) |  |  [optional] |
|**ratesAndBenefitsData** | [**AddCoupons200ResponseRatesAndBenefitsData**](AddCoupons200ResponseRatesAndBenefitsData.md) |  |  [optional] |
|**roundingError** | **Integer** | Rounding error. |  [optional] |
|**salesAssociateId** | **String** | Sales Associate (Seller) identification code. |  [optional] |
|**salesChannel** | **String** | Sales channel. |  [optional] |
|**sellerOrderId** | **String** | ID of the order in the seller. |  [optional] |
|**sellers** | [**List&lt;AddCoupons200ResponseSellersInner&gt;**](AddCoupons200ResponseSellersInner.md) | Information on each seller. |  [optional] |
|**shippingData** | [**AddCoupons200ResponseShippingData**](AddCoupons200ResponseShippingData.md) |  |  [optional] |
|**state** | **String** | State. |  [optional] |
|**storeId** | **String** | Store ID. |  [optional] |
|**timeZoneCreationDate** | **String** | Time zone creation date. |  [optional] |
|**timeZoneLastChange** | **String** | Time zone last change. |  [optional] |
|**totals** | [**List&lt;CartSimulation200ResponseLogisticsInfoInnerTotalsInner&gt;**](CartSimulation200ResponseLogisticsInfoInnerTotalsInner.md) | Information on order totals. |  [optional] |
|**userType** | **String** | User type. |  [optional] |
|**value** | **Integer** | Value of the order. |  [optional] |



