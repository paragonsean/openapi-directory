# CheckoutApi.AddPaymentDataRequestPaymentsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **String** | Payment system group. | [optional] [default to &#39;bankInvoicePaymentGroup&#39;]
**hasDefaultBillingAddress** | **Boolean** | Indicates whether billing address for this payment is the default address. | [optional] [default to false]
**installments** | **Number** | Selected number of installments. | [optional] [default to 1]
**installmentsInterestRate** | **Number** | Installments&#39; interest rate. | [optional] [default to 0]
**installmentsValue** | **Number** | Value of the installments. | [optional] [default to 1]
**paymentSystem** | **Number** | Payment system ID. | [optional] [default to 1]
**paymentSystemName** | **String** | Payment system name. | [optional] [default to &#39;Boleto Bancário&#39;]
**referenceValue** | **Number** | Reference value used to calculate total order value with interest. | [optional] [default to 100]
**value** | **Number** | Total value assigned to this payment. | [optional] [default to 100]


