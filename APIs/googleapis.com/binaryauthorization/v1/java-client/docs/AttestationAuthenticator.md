

# AttestationAuthenticator

An attestation authenticator that will be used to verify attestations. Typically this is just a set of public keys. Conceptually, an authenticator can be treated as always returning either \"authenticated\" or \"not authenticated\" when presented with a signed attestation (almost always assumed to be a [DSSE](https://github.com/secure-systems-lab/dsse) attestation). The details of how an authenticator makes this decision are specific to the type of 'authenticator' that this message wraps.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Optional. A user-provided name for this &#x60;AttestationAuthenticator&#x60;. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results. |  [optional] |
|**pkixPublicKeySet** | [**PkixPublicKeySet**](PkixPublicKeySet.md) |  |  [optional] |



