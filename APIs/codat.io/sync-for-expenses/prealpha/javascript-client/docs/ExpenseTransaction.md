# CodatExpenseApi.ExpenseTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | Currency the transaction was recorded in. | 
**currencyRate** | **Number** | Rate to convert the total amount of the payment into the base currency for the company at the time of the payment.  Currency rates in Codat are implemented as the multiple of foreign currency units to each base currency unit.    Where the currency rate is provided by the underlying accounting platform, it will be available from Codat with the same precision (up to a maximum of 9 decimal places).   For accounting platforms which do not provide an explicit currency rate, it is calculated as &#x60;baseCurrency / foreignCurrency&#x60; and will be returned to 9 decimal places.  ## Examples with base currency of GBP  | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (GBP) | | :--------------- | :------------- | :------------ | :------------------------- | | **USD**          | $20            | 0.781         | £15.62                     | | **EUR**          | €20            | 0.885         | £17.70                     | | **RUB**          | ₽20            | 0.011         | £0.22                      |  ## Examples with base currency of USD  | Foreign Currency | Foreign Amount | Currency Rate | Base Currency Amount (USD) | | :--------------- | :------------- | :------------ | :------------------------- | | **GBP**          | £20            | 1.277         | $25.54                     | | **EUR**          | €20            | 1.134         | $22.68                     | | **RUB**          | ₽20            | 0.015         | $0.30                      | | [optional] 
**id** | **String** | Your unique idenfier for the transaction. | 
**issueDate** | **String** | In Codat&#39;s data model, dates and times are represented using the &lt;a class&#x3D;\&quot;external\&quot; href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601 standard&lt;/a&gt;. Date and time fields are formatted as strings; for example:  &#x60;&#x60;&#x60; 2020-10-08T22:40:50Z 2021-01-01T00:00:00 &#x60;&#x60;&#x60;    When syncing data that contains &#x60;DateTime&#x60; fields from Codat, make sure you support the following cases when reading time information:  - Coordinated Universal Time (UTC): &#x60;2021-11-15T06:00:00Z&#x60; - Unqualified local time: &#x60;2021-11-15T01:00:00&#x60; - UTC time offsets: &#x60;2021-11-15T01:00:00-05:00&#x60;  &gt; Time zones &gt;  &gt; Not all dates from Codat will contain information about time zones.   &gt; Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced. | 
**lines** | [**[ExpenseTransactionLine]**](ExpenseTransactionLine.md) | Array of transaction lines. | [optional] 
**merchantName** | **String** | Name of the merchant where the purchase took place | [optional] 
**notes** | **String** | Any private, company notes about the transaction. | [optional] 
**type** | **String** | The type of transaction. | 



## Enum: TypeEnum


* `Payment` (value: `"Payment"`)

* `Refund` (value: `"Refund"`)

* `Reward` (value: `"Reward"`)

* `Chargeback` (value: `"Chargeback"`)

* `TransferIn` (value: `"TransferIn"`)

* `TransferOut` (value: `"TransferOut"`)

* `AdjustmentIn` (value: `"AdjustmentIn"`)

* `AdjustmentOut` (value: `"AdjustmentOut"`)




