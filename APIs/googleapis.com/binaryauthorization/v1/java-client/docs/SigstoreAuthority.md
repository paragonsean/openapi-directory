

# SigstoreAuthority

A Sigstore authority, used to verify signatures that are created by Sigstore. An authority is analogous to an attestation authenticator, verifying that a signature is valid or invalid.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Optional. A user-provided name for this &#x60;SigstoreAuthority&#x60;. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results. |  [optional] |
|**publicKeySet** | [**SigstorePublicKeySet**](SigstorePublicKeySet.md) |  |  [optional] |



