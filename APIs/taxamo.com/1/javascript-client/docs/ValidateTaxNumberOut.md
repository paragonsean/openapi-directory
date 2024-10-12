# Taxamo.ValidateTaxNumberOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingCountryCode** | **String** | Billing two letter ISO country code. | [optional] 
**buyerTaxNumber** | **String** |  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly. | [optional] 
**buyerTaxNumberValid** | **Boolean** | If the buyer tax number has been provided and was validated successfully. Always true for domestic transactions (billing country same as merchant&#39;s country), tax number doesn&#39;t get validated in that case. | [optional] 
**taxDeducted** | **Boolean** | If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example. | [optional] 


