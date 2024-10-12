

# TestOrderPaymentMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationMonth** | **Integer** | The card expiration month (January &#x3D; 1, February &#x3D; 2 etc.). |  [optional] |
|**expirationYear** | **Integer** | The card expiration year (4-digit, e.g. 2015). |  [optional] |
|**lastFourDigits** | **String** | The last four digits of the card number. |  [optional] |
|**predefinedBillingAddress** | **String** | The billing address. Acceptable values are: - \&quot;&#x60;dwight&#x60;\&quot; - \&quot;&#x60;jim&#x60;\&quot; - \&quot;&#x60;pam&#x60;\&quot;  |  [optional] |
|**type** | **String** | The type of instrument. Note that real orders might have different values than the four values accepted by &#x60;createTestOrder&#x60;. Acceptable values are: - \&quot;&#x60;AMEX&#x60;\&quot; - \&quot;&#x60;DISCOVER&#x60;\&quot; - \&quot;&#x60;MASTERCARD&#x60;\&quot; - \&quot;&#x60;VISA&#x60;\&quot;  |  [optional] |



