# AdyenCheckoutApi.AccountInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountAgeIndicator** | **String** | Indicator for the length of time since this shopper account was created in the merchant&#39;s environment. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days | [optional] 
**accountChangeDate** | **Date** | Date when the shopper&#39;s account was last changed. | [optional] 
**accountChangeIndicator** | **String** | Indicator for the length of time since the shopper&#39;s account was last updated. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days | [optional] 
**accountCreationDate** | **Date** | Date when the shopper&#39;s account was created. | [optional] 
**addCardAttemptsDay** | **Number** | Number of attempts the shopper tried to add a card to their account in the last day. | [optional] 
**deliveryAddressUsageDate** | **Date** | Date the selected delivery address was first used. | [optional] 
**deliveryAddressUsageIndicator** | **String** | Indicator for the length of time since this delivery address was first used. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days | [optional] 
**homePhone** | **String** | Shopper&#39;s home phone number (including the country code). | [optional] 
**mobilePhone** | **String** | Shopper&#39;s mobile phone number (including the country code). | [optional] 
**passwordChangeDate** | **Date** | Date when the shopper last changed their password. | [optional] 
**passwordChangeIndicator** | **String** | Indicator when the shopper has changed their password. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days | [optional] 
**pastTransactionsDay** | **Number** | Number of all transactions (successful and abandoned) from this shopper in the past 24 hours. | [optional] 
**pastTransactionsYear** | **Number** | Number of all transactions (successful and abandoned) from this shopper in the past year. | [optional] 
**paymentAccountAge** | **Date** | Date this payment method was added to the shopper&#39;s account. | [optional] 
**paymentAccountIndicator** | **String** | Indicator for the length of time since this payment method was added to this shopper&#39;s account. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days | [optional] 
**purchasesLast6Months** | **Number** | Number of successful purchases in the last six months. | [optional] 
**suspiciousActivity** | **Boolean** | Whether suspicious activity was recorded on this account. | [optional] 
**workPhone** | **String** | Shopper&#39;s work phone number (including the country code). | [optional] 



## Enum: AccountAgeIndicatorEnum


* `notApplicable` (value: `"notApplicable"`)

* `thisTransaction` (value: `"thisTransaction"`)

* `lessThan30Days` (value: `"lessThan30Days"`)

* `from30To60Days` (value: `"from30To60Days"`)

* `moreThan60Days` (value: `"moreThan60Days"`)





## Enum: AccountChangeIndicatorEnum


* `thisTransaction` (value: `"thisTransaction"`)

* `lessThan30Days` (value: `"lessThan30Days"`)

* `from30To60Days` (value: `"from30To60Days"`)

* `moreThan60Days` (value: `"moreThan60Days"`)





## Enum: DeliveryAddressUsageIndicatorEnum


* `thisTransaction` (value: `"thisTransaction"`)

* `lessThan30Days` (value: `"lessThan30Days"`)

* `from30To60Days` (value: `"from30To60Days"`)

* `moreThan60Days` (value: `"moreThan60Days"`)





## Enum: PasswordChangeIndicatorEnum


* `notApplicable` (value: `"notApplicable"`)

* `thisTransaction` (value: `"thisTransaction"`)

* `lessThan30Days` (value: `"lessThan30Days"`)

* `from30To60Days` (value: `"from30To60Days"`)

* `moreThan60Days` (value: `"moreThan60Days"`)





## Enum: PaymentAccountIndicatorEnum


* `notApplicable` (value: `"notApplicable"`)

* `thisTransaction` (value: `"thisTransaction"`)

* `lessThan30Days` (value: `"lessThan30Days"`)

* `from30To60Days` (value: `"from30To60Days"`)

* `moreThan60Days` (value: `"moreThan60Days"`)




