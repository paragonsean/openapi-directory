

# PaymentDetail

Information about payment related to a reservation order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | Shows the Account that is charged for this payment. |  [optional] |
|**billingCurrencyTotal** | [**Price**](Price.md) |  |  [optional] |
|**dueDate** | **LocalDate** | Date when the payment needs to be done. |  [optional] |
|**extendedStatusInfo** | [**ExtendedStatusInfo**](ExtendedStatusInfo.md) |  |  [optional] |
|**paymentDate** | **LocalDate** | Date when the transaction is completed. Is null when it is scheduled. |  [optional] |
|**pricingCurrencyTotal** | [**Price**](Price.md) |  |  [optional] |
|**status** | **PaymentStatus** |  |  [optional] |



