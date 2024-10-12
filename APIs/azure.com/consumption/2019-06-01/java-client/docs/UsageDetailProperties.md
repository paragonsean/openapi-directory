

# UsageDetailProperties

The properties of the usage detail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | Account Name. |  [optional] [readonly] |
|**accountOwnerId** | **String** | Account Owner Id. |  [optional] [readonly] |
|**additionalInfo** | **String** | Additional details of this usage item. By default this is not populated, unless it&#39;s specified in $expand. Use this field to get usage line item specific details such as the actual VM Size (ServiceType) or the ratio in which the reservation discount is applied. |  [optional] [readonly] |
|**billingAccountId** | **String** | Billing Account identifier. |  [optional] [readonly] |
|**billingAccountName** | **String** | Billing Account Name. |  [optional] [readonly] |
|**billingCurrency** | **String** | Billing Currency. |  [optional] [readonly] |
|**billingPeriodEndDate** | **OffsetDateTime** | The billing period end date. |  [optional] [readonly] |
|**billingPeriodStartDate** | **OffsetDateTime** | The billing period start date. |  [optional] [readonly] |
|**billingProfileId** | **String** | Billing Profile identifier. |  [optional] [readonly] |
|**billingProfileName** | **String** | Billing Profile Name. |  [optional] [readonly] |
|**chargeType** | **String** | Indicates a charge represents credits, usage, a Marketplace purchase, a reservation fee, or a refund. |  [optional] [readonly] |
|**consumedService** | **String** | Consumed service name. Name of the azure resource provider that emits the usage or was purchased. This value is not provided for marketplace usage. |  [optional] [readonly] |
|**cost** | **BigDecimal** | The amount of cost before tax. |  [optional] [readonly] |
|**costCenter** | **String** | The cost center of this department if it is a department and a cost center is provided. |  [optional] [readonly] |
|**date** | **OffsetDateTime** | Date for the usage record. |  [optional] [readonly] |
|**effectivePrice** | **BigDecimal** | Effective Price that&#39;s charged for the usage. |  [optional] [readonly] |
|**frequency** | **String** | Indicates how frequently this charge will occur. OneTime for purchases which only happen once, Monthly for fees which recur every month, and UsageBased for charges based on how much a service is used. |  [optional] [readonly] |
|**invoiceSection** | **String** | Invoice Section Name. |  [optional] [readonly] |
|**isAzureCreditEligible** | **Boolean** | Is Azure Credit Eligible. |  [optional] [readonly] |
|**meterDetails** | [**MeterDetailsResponse**](MeterDetailsResponse.md) |  |  [optional] |
|**meterId** | **UUID** | The meter id (GUID). Not available for marketplace. For reserved instance this represents the primary meter for which the reservation was purchased. For the actual VM Size for which the reservation is purchased see productOrderName. |  [optional] [readonly] |
|**offerId** | **String** | Offer Id. Ex: MS-AZR-0017P, MS-AZR-0148P. |  [optional] [readonly] |
|**partNumber** | **String** | Part Number of the service used. Can be used to join with the price sheet. Not available for marketplace. |  [optional] [readonly] |
|**planName** | **String** | Plan Name. |  [optional] [readonly] |
|**product** | **String** | Product name for the consumed service or purchase. Not available for Marketplace. |  [optional] [readonly] |
|**productOrderId** | **String** | Product Order Id. For reservations this is the Reservation Order ID. |  [optional] [readonly] |
|**productOrderName** | **String** | Product Order Name. For reservations this is the SKU that was purchased. |  [optional] [readonly] |
|**publisherName** | **String** | Publisher Name. |  [optional] [readonly] |
|**publisherType** | **String** | Publisher Type. |  [optional] [readonly] |
|**quantity** | **BigDecimal** | The usage quantity. |  [optional] [readonly] |
|**reservationId** | **String** | ARM resource id of the reservation. Only applies to records relevant to reservations. |  [optional] [readonly] |
|**reservationName** | **String** | User provided display name of the reservation. Last known name for a particular day is populated in the daily data. Only applies to records relevant to reservations. |  [optional] [readonly] |
|**resourceGroup** | **String** | Resource Group Name. |  [optional] [readonly] |
|**resourceId** | **String** | Azure resource manager resource identifier. |  [optional] [readonly] |
|**resourceLocation** | **String** | Resource Location. |  [optional] [readonly] |
|**resourceName** | **String** | Resource Name. |  [optional] [readonly] |
|**serviceInfo1** | **String** | Service Info 1. |  [optional] [readonly] |
|**serviceInfo2** | **String** | Service Info 2. |  [optional] [readonly] |
|**subscriptionId** | **String** | Subscription guid. |  [optional] [readonly] |
|**subscriptionName** | **String** | Subscription name. |  [optional] [readonly] |
|**term** | **String** | Term (in months). 1 month for monthly recurring purchase. 12 months for a 1 year reservation. 36 months for a 3 year reservation. |  [optional] [readonly] |
|**unitPrice** | **BigDecimal** | Unit Price is the price applicable to you. (your EA or other contract price). |  [optional] [readonly] |



