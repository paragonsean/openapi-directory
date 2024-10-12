# SquareConnectApi.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canceledDate** | **String** | The subscription cancellation date, in YYYY-MM-DD format (for example, 2013-01-15). On this date, the subscription status changes to &#x60;CANCELED&#x60; and the subscription billing stops. If you don&#39;t set this field, the subscription plan dictates if and when subscription ends.  You cannot update this field, you can only clear it. | [optional] 
**cardId** | **String** | The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) [card](https://developer.squareup.com/reference/square_2021-08-18/objects/Card) that is charged for the subscription. | [optional] 
**chargedThroughDate** | **String** | The date up to which the customer is invoiced for the subscription, in YYYY-MM-DD format (for example, 2013-01-15).  After the invoice is sent for a given billing period, this date will be the last day of the billing period. For example, suppose for the month of May a customer gets an invoice (or charged the card) on May 1. For the monthly billing scenario, this date is then set to May 31. | [optional] 
**createdAt** | **String** | The timestamp when the subscription was created, in RFC 3339 format. | [optional] 
**customerId** | **String** | The ID of the associated [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) profile. | [optional] 
**id** | **String** | The Square-assigned ID of the subscription. | [optional] 
**invoiceIds** | **[String]** | The IDs of the [invoices](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) created for the subscription, listed in order when the invoices were created (oldest invoices appear first). | [optional] 
**locationId** | **String** | The ID of the location associated with the subscription. | [optional] 
**planId** | **String** | The ID of the associated [subscription plan](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogSubscriptionPlan). | [optional] 
**priceOverrideMoney** | [**Money**](Money.md) |  | [optional] 
**startDate** | **String** | The start date of the subscription, in YYYY-MM-DD format (for example, 2013-01-15). | [optional] 
**status** | **String** | The current status of the subscription. | [optional] 
**taxPercentage** | **String** | The tax amount applied when billing the subscription. The percentage is expressed in decimal form, using a &#x60;&#39;.&#39;&#x60; as the decimal separator and without a &#x60;&#39;%&#39;&#x60; sign. For example, a value of &#x60;7.5&#x60; corresponds to 7.5%. | [optional] 
**timezone** | **String** | Timezone that will be used in date calculations for the subscription. Defaults to the timezone of the location based on &#x60;location_id&#x60;. Format: the IANA Timezone Database identifier for the location timezone (for example, &#x60;America/Los_Angeles&#x60;). | [optional] 
**version** | **Number** | The version of the object. When updating an object, the version supplied must match the version in the database, otherwise the write will be rejected as conflicting. | [optional] 


