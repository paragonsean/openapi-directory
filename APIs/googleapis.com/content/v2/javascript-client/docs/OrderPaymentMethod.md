# ContentApiForShopping.OrderPaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**OrderAddress**](OrderAddress.md) |  | [optional] 
**expirationMonth** | **Number** | The card expiration month (January &#x3D; 1, February &#x3D; 2 etc.). | [optional] 
**expirationYear** | **Number** | The card expiration year (4-digit, e.g. 2015). | [optional] 
**lastFourDigits** | **String** | The last four digits of the card number. | [optional] 
**phoneNumber** | **String** | The billing phone number. | [optional] 
**type** | **String** | The type of instrument. Acceptable values are: - \&quot;&#x60;AMEX&#x60;\&quot; - \&quot;&#x60;DISCOVER&#x60;\&quot; - \&quot;&#x60;JCB&#x60;\&quot; - \&quot;&#x60;MASTERCARD&#x60;\&quot; - \&quot;&#x60;UNIONPAY&#x60;\&quot; - \&quot;&#x60;VISA&#x60;\&quot; - \&quot;&#x60;&#x60;\&quot;  | [optional] 


