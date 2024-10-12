

# InvoiceResponseClarification

A clarification for why a received invoice was rejected (RE) or under query (UQ) and what action to take.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clarification** | **String** | A textual description of the clarification |  [optional] |
|**clarificationCode** | [**ClarificationCodeEnum**](#ClarificationCodeEnum) | The code for the clarification. For details see https://docs.peppol.eu/poacc/upgrade-3/codelist/OPStatusReason/ and https://docs.peppol.eu/poacc/upgrade-3/codelist/OPStatusAction/ |  [optional] |
|**clarificationCodeType** | [**ClarificationCodeTypeEnum**](#ClarificationCodeTypeEnum) | The type of the clarification. |  [optional] |
|**conditions** | [**List&lt;InvoiceResponseCondition&gt;**](InvoiceResponseCondition.md) | A list of conditions that triggered the error. This is only included for receiving in webhooks. You cannot currently send these conditions. |  [optional] |



## Enum: ClarificationCodeEnum

| Name | Value |
|---- | -----|
| NON | &quot;NON&quot; |
| REF | &quot;REF&quot; |
| LEG | &quot;LEG&quot; |
| REC | &quot;REC&quot; |
| QUA | &quot;QUA&quot; |
| DEL | &quot;DEL&quot; |
| PRI | &quot;PRI&quot; |
| QTY | &quot;QTY&quot; |
| ITM | &quot;ITM&quot; |
| PAY | &quot;PAY&quot; |
| UNR | &quot;UNR&quot; |
| FIN | &quot;FIN&quot; |
| PPD | &quot;PPD&quot; |
| OTH | &quot;OTH&quot; |
| NOA | &quot;NOA&quot; |
| PIN | &quot;PIN&quot; |
| NIN | &quot;NIN&quot; |
| CNF | &quot;CNF&quot; |
| CNP | &quot;CNP&quot; |
| CNA | &quot;CNA&quot; |



## Enum: ClarificationCodeTypeEnum

| Name | Value |
|---- | -----|
| OP_STATUS_REASON | &quot;OPStatusReason&quot; |
| OP_STATUS_ACTION | &quot;OPStatusAction&quot; |



