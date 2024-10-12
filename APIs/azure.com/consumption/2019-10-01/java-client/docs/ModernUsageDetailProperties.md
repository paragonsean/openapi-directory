

# ModernUsageDetailProperties

The properties of the usage detail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | **String** | Additional details of this usage item. Use this field to get usage line item specific details such as the actual VM Size (ServiceType) or the ratio in which the reservation discount is applied. |  [optional] [readonly] |
|**billingAccountId** | **String** | Billing Account identifier. |  [optional] [readonly] |
|**billingAccountName** | **String** | Name of the Billing Account. |  [optional] [readonly] |
|**billingCurrencyCode** | **String** | The currency defining the billed cost. |  [optional] [readonly] |
|**billingPeriodEndDate** | **OffsetDateTime** | Billing Period End Date as in the invoice. |  [optional] [readonly] |
|**billingPeriodStartDate** | **OffsetDateTime** | Billing Period Start Date as in the invoice. |  [optional] [readonly] |
|**billingProfileId** | **String** | Identifier for the billing profile that groups costs across invoices in the a singular billing currency across across the customers who have onboarded the Microsoft customer agreement and the customers in CSP who have made entitlement purchases like SaaS, Marketplace, RI, etc. |  [optional] [readonly] |
|**billingProfileName** | **String** | Name of the billing profile that groups costs across invoices in the a singular billing currency across across the customers who have onboarded the Microsoft customer agreement and the customers in CSP who have made entitlement purchases like SaaS, Marketplace, RI, etc. |  [optional] [readonly] |
|**chargeType** | **String** | Indicates a charge represents credits, usage, a Marketplace purchase, a reservation fee, or a refund. |  [optional] [readonly] |
|**consumedService** | **String** | Consumed service name. Name of the azure resource provider that emits the usage or was purchased. This value is not provided for marketplace usage. |  [optional] [readonly] |
|**costCenter** | **String** | The cost center of this department if it is a department and a cost center is provided. |  [optional] [readonly] |
|**costInBillingCurrency** | **BigDecimal** | ExtendedCost or blended cost before tax in billed currency. |  [optional] [readonly] |
|**costInPricingCurrency** | **BigDecimal** | ExtendedCost or blended cost before tax in pricing currency to correlate with prices. |  [optional] [readonly] |
|**costInUSD** | **BigDecimal** | Estimated extendedCost or blended cost before tax in USD. |  [optional] [readonly] |
|**customerName** | **String** | Name of the customer&#39;s AAD tenant. |  [optional] [readonly] |
|**customerTenantId** | **String** | Identifier of the customer&#39;s AAD tenant. |  [optional] [readonly] |
|**date** | **OffsetDateTime** | Date for the usage record. |  [optional] [readonly] |
|**exchangeRate** | **String** | Exchange rate used in conversion from pricing currency to billing currency. |  [optional] [readonly] |
|**exchangeRateDate** | **OffsetDateTime** | Date on which exchange rate used in conversion from pricing currency to billing currency. |  [optional] [readonly] |
|**exchangeRatePricingToBilling** | **BigDecimal** | Exchange Rate from pricing currency to billing currency. |  [optional] [readonly] |
|**frequency** | **String** | Indicates how frequently this charge will occur. OneTime for purchases which only happen once, Monthly for fees which recur every month, and UsageBased for charges based on how much a service is used. |  [optional] [readonly] |
|**instanceName** | **String** | Instance Name. |  [optional] [readonly] |
|**invoiceId** | **String** | Invoice ID as on the invoice where the specific transaction appears. |  [optional] [readonly] |
|**invoiceSectionId** | **String** | Identifier of the project that is being charged in the invoice. Not applicable for Microsoft Customer Agreements onboarded by partners. |  [optional] [readonly] |
|**invoiceSectionName** | **String** | Name of the project that is being charged in the invoice. Not applicable for Microsoft Customer Agreements onboarded by partners. |  [optional] [readonly] |
|**isAzureCreditEligible** | **Boolean** | Determines if the cost is eligible to be paid for using Azure credits. |  [optional] [readonly] |
|**marketPrice** | **BigDecimal** | Market Price that&#39;s charged for the usage. |  [optional] [readonly] |
|**meterCategory** | **String** | Identifies the top-level service for the usage. |  [optional] [readonly] |
|**meterId** | **UUID** | The meter id (GUID). Not available for marketplace. For reserved instance this represents the primary meter for which the reservation was purchased. For the actual VM Size for which the reservation is purchased see productOrderName. |  [optional] [readonly] |
|**meterName** | **String** | Identifies the name of the meter against which consumption is measured. |  [optional] [readonly] |
|**meterRegion** | **String** | Identifies the location of the datacenter for certain services that are priced based on datacenter location. |  [optional] [readonly] |
|**meterSubCategory** | **String** | Defines the type or sub-category of Azure service that can affect the rate. |  [optional] [readonly] |
|**partnerEarnedCreditApplied** | **String** | Flag to indicate if partner earned credit has been applied or not. |  [optional] [readonly] |
|**partnerEarnedCreditRate** | **BigDecimal** | Rate of discount applied if there is a partner earned credit (PEC) based on partner admin link access. |  [optional] [readonly] |
|**partnerName** | **String** | Name of the partner&#39; AAD tenant. |  [optional] [readonly] |
|**partnerTenantId** | **String** | Identifier for the partner&#39;s AAD tenant. |  [optional] [readonly] |
|**paygCostInBillingCurrency** | **BigDecimal** | The amount of PayG cost before tax in billing currency. |  [optional] [readonly] |
|**paygCostInUSD** | **BigDecimal** | The amount of PayG cost before tax in US Dollar currency. |  [optional] [readonly] |
|**previousInvoiceId** | **String** | Reference to an original invoice there is a refund (negative cost). This is populated only when there is a refund. |  [optional] [readonly] |
|**pricingCurrencyCode** | **String** | Pricing Billing Currency. |  [optional] [readonly] |
|**product** | **String** | Name of the product that has accrued charges by consumption or purchase as listed in the invoice. Not available for Marketplace. |  [optional] [readonly] |
|**productIdentifier** | **String** | Identifer for the product that has accrued charges by consumption or purchase . This is the concatenated key of productId and SKuId in partner center. |  [optional] [readonly] |
|**productOrderId** | **String** | The identifier for the asset or Azure plan name that the subscription belongs to. For example: Azure Plan. For reservations this is the Reservation Order ID. |  [optional] [readonly] |
|**productOrderName** | **String** | Product Order Name. For reservations this is the SKU that was purchased. |  [optional] [readonly] |
|**publisherId** | **String** | Publisher Id. |  [optional] [readonly] |
|**publisherName** | **String** | Name of the publisher of the service including Microsoft or Third Party publishers. |  [optional] [readonly] |
|**publisherType** | **String** | Type of publisher that identifies if the publisher is first party, third party reseller or third party agency. |  [optional] [readonly] |
|**quantity** | **BigDecimal** | Measure the quantity purchased or consumed.The amount of the meter used during the billing period. |  [optional] [readonly] |
|**resellerMpnId** | **String** | MPNId for the reseller associated with the subscription. |  [optional] [readonly] |
|**resellerName** | **String** | Reseller Name. |  [optional] [readonly] |
|**reservationId** | **String** | ARM resource id of the reservation. Only applies to records relevant to reservations. |  [optional] [readonly] |
|**reservationName** | **String** | User provided display name of the reservation. Last known name for a particular day is populated in the daily data. Only applies to records relevant to reservations. |  [optional] [readonly] |
|**resourceGroup** | **String** | Name of the Azure resource group used for cohesive lifecycle management of resources. |  [optional] [readonly] |
|**resourceLocation** | **String** | Name of the resource location. |  [optional] [readonly] |
|**resourceLocationNormalized** | **String** | Resource Location Normalized. |  [optional] [readonly] |
|**serviceFamily** | **String** | List the service family for the product purchased or charged (Example: Storage ; Compute). |  [optional] [readonly] |
|**serviceInfo1** | **String** | Service Info 1. |  [optional] [readonly] |
|**serviceInfo2** | **String** | Service Info 2. |  [optional] [readonly] |
|**servicePeriodEndDate** | **OffsetDateTime** | End date for the period when the service usage was rated for charges. The prices for Azure services are determined based on the rating period. |  [optional] [readonly] |
|**servicePeriodStartDate** | **OffsetDateTime** | Start date for the rating period when the service usage was rated for charges. The prices for Azure services are determined for the rating period. |  [optional] [readonly] |
|**subscriptionGuid** | **String** | Unique Microsoft generated identifier for the Azure Subscription. |  [optional] [readonly] |
|**subscriptionName** | **String** | Name of the Azure Subscription. |  [optional] [readonly] |
|**term** | **String** | Term (in months). Displays the term for the validity of the offer. For example. In case of reserved instances it displays 12 months for yearly term of reserved instance. For one time purchases or recurring purchases, the terms displays 1 month; This is not applicable for Azure consumption. |  [optional] [readonly] |
|**unitOfMeasure** | **String** | Identifies the Unit that the service is charged in. For example, GB, hours, 10,000 s. |  [optional] [readonly] |
|**unitPrice** | **BigDecimal** | Unit Price is the price applicable to you. (your EA or other contract price). |  [optional] [readonly] |



