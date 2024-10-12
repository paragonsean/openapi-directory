

# ContentKeyPolicyTokenRestriction

Represents a token restriction. Provided token must match these requirements for successful license or key delivery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateVerificationKeys** | [**List&lt;ContentKeyPolicyRestrictionTokenKey&gt;**](ContentKeyPolicyRestrictionTokenKey.md) | A list of alternative verification keys. |  [optional] |
|**audience** | **String** | The audience for the token. |  |
|**issuer** | **String** | The token issuer. |  |
|**openIdConnectDiscoveryDocument** | **String** | The OpenID connect discovery document. |  [optional] |
|**primaryVerificationKey** | [**ContentKeyPolicyRestrictionTokenKey**](ContentKeyPolicyRestrictionTokenKey.md) |  |  |
|**requiredClaims** | [**List&lt;ContentKeyPolicyTokenClaim&gt;**](ContentKeyPolicyTokenClaim.md) | A list of required token claims. |  [optional] |
|**restrictionTokenType** | [**RestrictionTokenTypeEnum**](#RestrictionTokenTypeEnum) | The type of token. |  |



## Enum: RestrictionTokenTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| SWT | &quot;Swt&quot; |
| JWT | &quot;Jwt&quot; |



