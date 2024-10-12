# BeanstreamPayments.ProfileFromCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvd** | **String** | Security code on the back of the credit card. This can be set to mandatory in the back office. digits(3) | [optional] [default to &#39;123&#39;]
**expiryMonth** | **String** | eg. 02 for February. digits(2) | [default to &#39;02&#39;]
**expiryYear** | **String** | digits(2) | [default to &#39;18&#39;]
**name** | **String** | Card holder name. alphanumeric(64) | [default to &#39;5100000010001004&#39;]
**number** | **String** | Credit card number (PAN)  digits(20) | 


