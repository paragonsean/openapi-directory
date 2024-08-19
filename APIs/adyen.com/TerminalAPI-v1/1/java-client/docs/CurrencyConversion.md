

# CurrencyConversion

A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt). Information related to a currency conversion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commission** | **BigDecimal** | Commission for a currency conversion. |  [optional] |
|**convertedAmount** | [**ConvertedAmount**](ConvertedAmount.md) |  |  |
|**customerApprovedFlag** | **Boolean** | Notify if the customer has approved something. Indicates if the customer has accepted a currency conversion. |  [optional] |
|**declaration** | **String** | If a declaration has to be presented to the customer. |  [optional] |
|**markup** | **String** | Markup of a currency conversion amount as a percentage. |  [optional] |
|**rate** | **String** | Rate of currency conversion. |  [optional] |



