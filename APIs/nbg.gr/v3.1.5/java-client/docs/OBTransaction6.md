

# OBTransaction6

Provides further details on an entry in the report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner. |  |
|**amount** | [**OBActiveOrHistoricCurrencyAndAmount**](OBActiveOrHistoricCurrencyAndAmount.md) |  |  |
|**balance** | [**OBTransactionCashBalance**](OBTransactionCashBalance.md) |  |  [optional] |
|**bookingDateTime** | **OffsetDateTime** | Date and time when a transaction entry is posted to an account on the account servicer&#39;s books.  Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  |
|**creditDebitIndicator** | **OBCreditDebitCode** |  |  |
|**creditorAccount** | [**OBCashAccount6**](OBCashAccount6.md) |  |  [optional] |
|**debtorAccount** | [**OBCashAccount6**](OBCashAccount6.md) |  |  [optional] |
|**proprietaryBankTransactionCode** | [**ProprietaryBankTransactionCodeStructure1**](ProprietaryBankTransactionCodeStructure1.md) |  |  [optional] |
|**status** | **OBEntryStatus1Code** |  |  |
|**transactionInformation** | **String** | Further details of the transaction.  This is the transaction narrative, which is unstructured text. |  [optional] |
|**transactionReference** | **String** | Unique reference for the transaction. This reference is optionally populated, and may as an example be the FPID in the Faster Payments context. |  [optional] |
|**valueDateTime** | **OffsetDateTime** | Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry.  Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date.  For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used.In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  [optional] |



