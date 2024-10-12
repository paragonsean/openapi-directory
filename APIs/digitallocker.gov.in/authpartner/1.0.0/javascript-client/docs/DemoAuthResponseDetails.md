# AuthorizedPartnerApiSpecification.DemoAuthResponseDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token that can be used to call the DigiLocker APIs. | 
**expiresIn** | **String** | The duration in seconds for which the access token is valid. | 
**mobile** | **Number** | The masked mobile number of the user on which the OTP has been sent.            | 
**refreshToken** | **String** | The refresh token used to refresh the above access token when it expires. Please refer to Refresh Access Token API for more details. | 
**scope** | **String** | Scope of the token | 
**tokenType** | **String** | The type of token which will always be Bearer. | 


