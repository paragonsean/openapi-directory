

# MoneyObject

Provides information about a value of money. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The ISO 4217 currency code.  |  |
|**value** | **String** | The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be &#x60;\&quot;10.56\&quot;&#x60;. The currency symbol is not included in the string.  |  |
|**valueInBaseUnits** | **Integer** | The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be &#x60;1056&#x60;.  |  |



