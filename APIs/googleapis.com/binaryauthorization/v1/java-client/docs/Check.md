

# Check

A single check to perform against a Pod. Checks are grouped into `CheckSet` objects, which are defined by the top-level policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alwaysDeny** | **Boolean** | Optional. A special-case check that always denies. Note that this still only applies when the scope of the &#x60;CheckSet&#x60; applies and the image isn&#39;t exempted by an image allowlist. This check is primarily useful for testing, or to set the default behavior for all unmatched scopes to \&quot;deny\&quot;. |  [optional] |
|**displayName** | **String** | Optional. A user-provided name for this check. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results. |  [optional] |
|**imageAllowlist** | [**ImageAllowlist**](ImageAllowlist.md) |  |  [optional] |
|**imageFreshnessCheck** | [**ImageFreshnessCheck**](ImageFreshnessCheck.md) |  |  [optional] |
|**sigstoreSignatureCheck** | [**SigstoreSignatureCheck**](SigstoreSignatureCheck.md) |  |  [optional] |
|**simpleSigningAttestationCheck** | [**SimpleSigningAttestationCheck**](SimpleSigningAttestationCheck.md) |  |  [optional] |
|**slsaCheck** | [**SlsaCheck**](SlsaCheck.md) |  |  [optional] |
|**trustedDirectoryCheck** | [**TrustedDirectoryCheck**](TrustedDirectoryCheck.md) |  |  [optional] |
|**vulnerabilityCheck** | [**VulnerabilityCheck**](VulnerabilityCheck.md) |  |  [optional] |



