# Taxamo.CalculateTaxLocationOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingCountryCode** | **String** | Billing two letter ISO country code. | [optional] 
**buyerCreditCardPrefix** | **String** | First 6 digits of buyer&#39;s credit card prefix. | [optional] 
**buyerIp** | **String** | IP address of the buyer in dotted decimal (IPv4) or text format (IPv6). | [optional] 
**countries** | [**Countries**](Countries.md) |  | [optional] 
**evidence** | [**Evidence**](Evidence.md) |  | [optional] 
**taxCountryCode** | **String** | Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode. | [optional] 
**taxDeducted** | **Boolean** | If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example. | [optional] 
**taxSupported** | **Boolean** | Is tax calculation supported for a detected tax location? | [optional] 


