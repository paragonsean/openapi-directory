# BeanstreamPayments.Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **Boolean** | set to false for Pre-Authorize, and true to complete a payment | [optional] [default to true]
**cvd** | **String** | Security code on the back of the credit card. This can be set to mandatory in the back office. digits(3 or 4) | [optional] [default to &#39;123&#39;]
**expiryMonth** | **String** | eg. 02 for February. digits(2) | [default to &#39;02&#39;]
**expiryYear** | **String** | eg. 15 for 2015. digits(2) | [default to &#39;18&#39;]
**name** | **String** | Card holder name. alphanumeric(64) | 
**number** | **String** | Credit card number (PAN). digits(20) | [default to &#39;5100000010001004&#39;]


