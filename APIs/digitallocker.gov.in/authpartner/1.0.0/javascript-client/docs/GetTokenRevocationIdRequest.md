# AuthorizedPartnerApiSpecification.GetTokenRevocationIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **String** | The token that needs to be revoked. | 
**tokenTypeHint** | **String** | The type of the above token. The value will be one of access_token or refresh_token. If this parameter is not sent, DigiLocker will look for this token in both access and refresh tokens and then revoke it. | [optional] 



## Enum: TokenTypeHintEnum


* `refresh_token` (value: `"refresh_token"`)

* `access_token` (value: `"access_token"`)




