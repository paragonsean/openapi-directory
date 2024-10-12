# MdesCustomerService.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountPanSuffix** | **String** | Last 4 digits of Account PAN mapped (or to be mapped) to Token(s). | [optional] 
**alternateAccountIdentifierSuffix** | **String** | Alternate Account Identifier is a cardholder friendly reference to a bank account. It is typically used to identify associated tokens when the cardholder is unaware of their Account PAN. The Alternate Account Identifier Suffix exposes just the last few characters of the full identifier in order to protect the full identifier from possible fraud. | [optional] 
**expirationDate** | **String** | Expiration date of Account PAN mapped (or to be mapped) to Token(s). &#39;MMYY&#39; Format. | [optional] 
**tokens** | [**Tokens**](Tokens.md) |  | [optional] 


