

# Token


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationExpiryDate** | **OffsetDateTime** | The authorization expiry date you got back from the payment service provider |  [optional] |
|**authorizationReference** | **String** | The authorization reference. This value is specific for different payment service providers. There will be              a page on the developer portal explaining the pattern on how to fill this value for the payment service              provider hetras is integrated with |  [optional] |
|**authorizationStatus** | [**AuthorizationStatusEnum**](#AuthorizationStatusEnum) | The authorization status you got back from the payment service provider |  [optional] |
|**authorizedAmount** | **Double** | The authorized amount |  [optional] |
|**merchantReference** | **String** | The merchant reference you used when requesting the token from the payment service provider |  [optional] |
|**shopperEmail** | **String** | The shopper email you used when requesting the token from the payment service provider |  [optional] |
|**shopperReference** | **String** | The shopper reference you used when requesting the token from the payment service provider. It can              be the same as the merchant reference |  [optional] |
|**tokenId** | **String** | The token id you get from the payment service provider |  [optional] |



## Enum: AuthorizationStatusEnum

| Name | Value |
|---- | -----|
| AUTHORIZED | &quot;Authorized&quot; |
| REFUSED | &quot;Refused&quot; |
| ERROR | &quot;Error&quot; |
| CANCELED | &quot;Canceled&quot; |
| CONSUMED | &quot;Consumed&quot; |
| AUTHORIZED_WITH_ZERO_AMOUNT | &quot;AuthorizedWithZeroAmount&quot; |



