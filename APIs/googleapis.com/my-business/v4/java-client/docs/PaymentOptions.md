

# PaymentOptions

Forms of payment accepted at the property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cash** | **Boolean** | Cash. The hotel accepts payment by paper/coin currency. |  [optional] |
|**cashException** | [**CashExceptionEnum**](#CashExceptionEnum) | Cash exception. |  [optional] |
|**cheque** | **Boolean** | Cheque. The hotel accepts a printed document issued by the guest&#39;s bank in the guest&#39;s name as a form of payment. |  [optional] |
|**chequeException** | [**ChequeExceptionEnum**](#ChequeExceptionEnum) | Cheque exception. |  [optional] |
|**creditCard** | **Boolean** | Credit card. The hotel accepts payment by a card issued by a bank or credit card company. Also known as charge card, debit card, bank card, or charge plate. |  [optional] |
|**creditCardException** | [**CreditCardExceptionEnum**](#CreditCardExceptionEnum) | Credit card exception. |  [optional] |
|**debitCard** | **Boolean** | Debit card. The hotel accepts a bank-issued card that immediately deducts the charged funds from the guest&#39;s bank account upon processing. |  [optional] |
|**debitCardException** | [**DebitCardExceptionEnum**](#DebitCardExceptionEnum) | Debit card exception. |  [optional] |
|**mobileNfc** | **Boolean** | Mobile nfc. The hotel has the compatible computer hardware terminal that reads and charges a payment app on the guest&#39;s smartphone without requiring the two devices to make physical contact. Also known as Apple Pay, Google Pay, Samsung Pay. |  [optional] |
|**mobileNfcException** | [**MobileNfcExceptionEnum**](#MobileNfcExceptionEnum) | Mobile nfc exception. |  [optional] |



## Enum: CashExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: ChequeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: CreditCardExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: DebitCardExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MobileNfcExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



