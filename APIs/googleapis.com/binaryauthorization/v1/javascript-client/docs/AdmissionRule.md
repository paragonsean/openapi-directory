# BinaryAuthorizationApi.AdmissionRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforcementMode** | **String** | Required. The action when a pod creation is denied by the admission rule. | [optional] 
**evaluationMode** | **String** | Required. How this admission rule will be evaluated. | [optional] 
**requireAttestationsBy** | **[String]** | Optional. The resource names of the attestors that must attest to a container image, in the format &#x60;projects/_*_/attestors/_*&#x60;. Each attestor must exist before a policy can reference it. To add an attestor to a policy the principal issuing the policy change request must be able to read the attestor resource. Note: this field must be non-empty when the &#x60;evaluation_mode&#x60; field specifies &#x60;REQUIRE_ATTESTATION&#x60;, otherwise it must be empty. | [optional] 



## Enum: EnforcementModeEnum


* `ENFORCEMENT_MODE_UNSPECIFIED` (value: `"ENFORCEMENT_MODE_UNSPECIFIED"`)

* `ENFORCED_BLOCK_AND_AUDIT_LOG` (value: `"ENFORCED_BLOCK_AND_AUDIT_LOG"`)

* `DRYRUN_AUDIT_LOG_ONLY` (value: `"DRYRUN_AUDIT_LOG_ONLY"`)





## Enum: EvaluationModeEnum


* `EVALUATION_MODE_UNSPECIFIED` (value: `"EVALUATION_MODE_UNSPECIFIED"`)

* `ALWAYS_ALLOW` (value: `"ALWAYS_ALLOW"`)

* `REQUIRE_ATTESTATION` (value: `"REQUIRE_ATTESTATION"`)

* `ALWAYS_DENY` (value: `"ALWAYS_DENY"`)




