

# ReservationOrderBillingPlanInformation

Information describing the type of billing plan for this reservation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPaymentDueDate** | **LocalDate** | For recurring billing plans, indicates the date when next payment will be processed. Null when total is paid off. |  [optional] |
|**pricingCurrencyTotal** | [**Price**](Price.md) |  |  [optional] |
|**startDate** | **LocalDate** | Date when the billing plan has started. |  [optional] |
|**transactions** | [**List&lt;PaymentDetail&gt;**](PaymentDetail.md) |  |  [optional] |



