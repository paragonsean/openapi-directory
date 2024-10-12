# CloudOsLoginApi.SecurityKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceNickname** | **String** | The security key nickname explicitly set by the user. | [optional] 
**privateKey** | **String** | Hardware-backed private key text in SSH format. | [optional] 
**publicKey** | **String** | Public key text in SSH format, defined by [RFC4253](\&quot;https://www.ietf.org/rfc/rfc4253.txt\&quot;) section 6.6. | [optional] 
**universalTwoFactor** | [**UniversalTwoFactor**](UniversalTwoFactor.md) |  | [optional] 
**webAuthn** | [**WebAuthn**](WebAuthn.md) |  | [optional] 


