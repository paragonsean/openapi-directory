# AdyenCheckoutApi.ResponseAdditionalDataInstallments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installmentPaymentDataInstallmentType** | **String** | Type of installment. The value of &#x60;installmentType&#x60; should be **IssuerFinanced**. | [optional] 
**installmentPaymentDataOptionItemNrAnnualPercentageRate** | **String** | Annual interest rate. | [optional] 
**installmentPaymentDataOptionItemNrFirstInstallmentAmount** | **String** | First Installment Amount in minor units. | [optional] 
**installmentPaymentDataOptionItemNrInstallmentFee** | **String** | Installment fee amount in minor units. | [optional] 
**installmentPaymentDataOptionItemNrInterestRate** | **String** | Interest rate for the installment period. | [optional] 
**installmentPaymentDataOptionItemNrMaximumNumberOfInstallments** | **String** | Maximum number of installments possible for this payment. | [optional] 
**installmentPaymentDataOptionItemNrMinimumNumberOfInstallments** | **String** | Minimum number of installments possible for this payment. | [optional] 
**installmentPaymentDataOptionItemNrNumberOfInstallments** | **String** | Total number of installments possible for this payment. | [optional] 
**installmentPaymentDataOptionItemNrSubsequentInstallmentAmount** | **String** | Subsequent Installment Amount in minor units. | [optional] 
**installmentPaymentDataOptionItemNrTotalAmountDue** | **String** | Total amount in minor units. | [optional] 
**installmentPaymentDataPaymentOptions** | **String** | Possible values: * PayInInstallmentsOnly * PayInFullOnly * PayInFullOrInstallments | [optional] 
**installmentsValue** | **String** | The number of installments that the payment amount should be charged with.  Example: 5 &gt; Only relevant for card payments in countries that support installments. | [optional] 


