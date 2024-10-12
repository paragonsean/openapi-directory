

# OBCashBalance1

Set of elements used to define the balance details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner. |  |
|**amount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  |
|**creditDebitIndicator** | **OBCreditDebitCode** |  |  |
|**creditLine** | [**List&lt;OBCreditLine1&gt;**](OBCreditLine1.md) | Set of elements used to provide details on the credit line. |  [optional] |
|**dateTime** | **OffsetDateTime** | Indicates the date (and time) of the balance.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 |  |
|**type** | **OBBalanceType1Code** |  |  |



