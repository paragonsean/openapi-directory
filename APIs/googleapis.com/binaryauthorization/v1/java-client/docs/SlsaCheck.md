

# SlsaCheck

A SLSA provenance attestation check, which ensures that images are built by a trusted builder using source code from its trusted repositories only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rules** | [**List&lt;VerificationRule&gt;**](VerificationRule.md) | Specifies a list of verification rules for the SLSA attestations. An image is considered compliant with the SlsaCheck if any of the rules are satisfied. |  [optional] |



