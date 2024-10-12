# AzureMediaServices.ContentKeyPolicyTokenRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateVerificationKeys** | [**[ContentKeyPolicyRestrictionTokenKey]**](ContentKeyPolicyRestrictionTokenKey.md) | A list of alternative verification keys. | [optional] 
**audience** | **String** | The audience for the token. | 
**issuer** | **String** | The token issuer. | 
**openIdConnectDiscoveryDocument** | **String** | The OpenID connect discovery document. | [optional] 
**primaryVerificationKey** | [**ContentKeyPolicyRestrictionTokenKey**](ContentKeyPolicyRestrictionTokenKey.md) |  | 
**requiredClaims** | [**[ContentKeyPolicyTokenClaim]**](ContentKeyPolicyTokenClaim.md) | A list of required token claims. | [optional] 
**restrictionTokenType** | **String** | The type of token. | 



## Enum: RestrictionTokenTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Swt` (value: `"Swt"`)

* `Jwt` (value: `"Jwt"`)




