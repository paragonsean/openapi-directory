# HetrasBookingApiVersion0.Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationExpiryDate** | **Date** | The authorization expiry date you got back from the payment service provider | [optional] 
**authorizationReference** | **String** | The authorization reference. This value is specific for different payment service providers. There will be              a page on the developer portal explaining the pattern on how to fill this value for the payment service              provider hetras is integrated with | [optional] 
**authorizationStatus** | **String** | The authorization status you got back from the payment service provider | [optional] 
**authorizedAmount** | **Number** | The authorized amount | [optional] 
**merchantReference** | **String** | The merchant reference you used when requesting the token from the payment service provider | [optional] 
**shopperEmail** | **String** | The shopper email you used when requesting the token from the payment service provider | [optional] 
**shopperReference** | **String** | The shopper reference you used when requesting the token from the payment service provider. It can              be the same as the merchant reference | [optional] 
**tokenId** | **String** | The token id you get from the payment service provider | [optional] 



## Enum: AuthorizationStatusEnum


* `Authorized` (value: `"Authorized"`)

* `Refused` (value: `"Refused"`)

* `Error` (value: `"Error"`)

* `Canceled` (value: `"Canceled"`)

* `Consumed` (value: `"Consumed"`)

* `AuthorizedWithZeroAmount` (value: `"AuthorizedWithZeroAmount"`)




