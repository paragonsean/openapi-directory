

# EOBObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkDate** | **String** | Date of check. If missing, default to the date when the request is made |  [optional] |
|**depositDate** | **String** | Date when EOB gets deposited. |  [optional] |
|**doctor** | **Integer** |  |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**insurancePayerId** | **String** |  |  |
|**insurancePayerName** | **String** |  |  |
|**insurancePayerTraceNumber** | **String** |  |  |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | &#x60;\&quot;\&quot;&#x60; - Unknown, &#x60;\&quot;ACH\&quot;&#x60; - Automated Clearing House (ACH), &#x60;\&quot;BOPCCP\&quot;&#x60; - Cash Concentration/Disbursement plus Addenda (CCD+) (ACH), &#x60;\&quot;BOPCTX\&quot;&#x60; - Corporate Trade Exchange (CTX) (ACH), &#x60;\&quot;CHK\&quot;&#x60; - Check, &#x60;\&quot;FWT\&quot;&#x60; - Federal Reserve Funds/Wire Transfer - Nonrepetitive, &#x60;\&quot;VPAY\&quot;&#x60; - vPayment, &#x60;\&quot;NON\&quot;&#x60; - Non-Payment Data |  [optional] |
|**postedDate** | **String** |  |  [optional] [readonly] |
|**scannedEob** | **String** |  |  [optional] |
|**totalPaid** | **BigDecimal** | Total amount paid. If missing, default to 0.00 |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| ACH | &quot;ACH&quot; |
| BOPCCP | &quot;BOPCCP&quot; |
| BOPCTX | &quot;BOPCTX&quot; |
| CHK | &quot;CHK&quot; |
| FWT | &quot;FWT&quot; |
| VPAY | &quot;VPAY&quot; |
| NON | &quot;NON&quot; |



