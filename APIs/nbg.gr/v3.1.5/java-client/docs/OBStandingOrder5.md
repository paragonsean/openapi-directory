

# OBStandingOrder5



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner. |  |
|**creditorAccount** | [**OBCashAccount5**](OBCashAccount5.md) |  |  [optional] |
|**finalPaymentAmount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  [optional] |
|**finalPaymentDateTime** | **OffsetDateTime** | The date on which the final payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  [optional] |
|**firstPaymentAmount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  [optional] |
|**firstPaymentDateTime** | **OffsetDateTime** | The date on which the first payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  [optional] |
|**frequency** | **String** | Individual Definitions:  IntrvlMnthDay - An interval specified in months(between 01, 02, 03, 04, 06, 12, 24), specifying the day within the month(01 to 31)  Full Regular Expression:  ^(IntrvlMnthDay:(0[1,2,3,4,6]|12|24):(0[1-9]|[12] [0-9]|3[01]))$ |  |
|**lastPaymentAmount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  [optional] |
|**lastPaymentDateTime** | **OffsetDateTime** | The date on which the last (most recent) payment for a Standing Order schedule was made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  [optional] |
|**nextPaymentAmount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  [optional] |
|**nextPaymentDateTime** | **OffsetDateTime** | The date on which the next payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  [optional] |
|**reference** | **String** | Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction.  Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money.  If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor&#39;s reference or payment remittance identification should be quoted in the end-to-end transaction identification. |  [optional] |
|**standingOrderId** | **String** | A unique and immutable identifier used to identify the standing order resource. This identifier has no meaning to the account owner. |  [optional] |
|**standingOrderStatusCode** | **OBExternalStandingOrderStatus1Code** |  |  [optional] |



