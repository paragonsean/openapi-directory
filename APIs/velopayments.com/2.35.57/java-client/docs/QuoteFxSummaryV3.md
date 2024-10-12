

# QuoteFxSummaryV3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Timestamp of when the quote was created |  |
|**expiryTime** | **OffsetDateTime** | The timestamp for when the quote will expire |  [optional] |
|**fundingStatus** | **String** | Current status of the funding associated with this quote. One of the following values: UNFUNDED, INSTRUCTED, FUNDED |  |
|**invertedRate** | **Float** | The inverse conversion rate (from paymnent currency to source currency) |  [optional] |
|**paymentCurrency** | **String** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. |  |
|**quoteId** | **UUID** | The id of the created quote |  |
|**rate** | **Float** | The conversion rate (from the source currency to the payment currency) |  |
|**sourceCurrency** | **String** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. |  |
|**status** | **String** | Current status of the fx quote. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED, REJECTED |  |
|**totalPaymentAmount** | **Integer** | The amount (in minor units) that the payee will receive |  |
|**totalSourceAmount** | **Integer** | The amount (in minor units) that will be paid from the source account |  |



