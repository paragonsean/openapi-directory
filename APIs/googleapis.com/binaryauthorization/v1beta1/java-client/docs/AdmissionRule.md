

# AdmissionRule

An admission rule specifies either that all container images used in a pod creation request must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be denied. Images matching an admission allowlist pattern are exempted from admission rules and will never block a pod creation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enforcementMode** | [**EnforcementModeEnum**](#EnforcementModeEnum) | Required. The action when a pod creation is denied by the admission rule. |  [optional] |
|**evaluationMode** | [**EvaluationModeEnum**](#EvaluationModeEnum) | Required. How this admission rule will be evaluated. |  [optional] |
|**requireAttestationsBy** | **List&lt;String&gt;** | Optional. The resource names of the attestors that must attest to a container image, in the format &#x60;projects/_*_/attestors/_*&#x60;. Each attestor must exist before a policy can reference it. To add an attestor to a policy the principal issuing the policy change request must be able to read the attestor resource. Note: this field must be non-empty when the evaluation_mode field specifies REQUIRE_ATTESTATION, otherwise it must be empty. |  [optional] |



## Enum: EnforcementModeEnum

| Name | Value |
|---- | -----|
| ENFORCEMENT_MODE_UNSPECIFIED | &quot;ENFORCEMENT_MODE_UNSPECIFIED&quot; |
| ENFORCED_BLOCK_AND_AUDIT_LOG | &quot;ENFORCED_BLOCK_AND_AUDIT_LOG&quot; |
| DRYRUN_AUDIT_LOG_ONLY | &quot;DRYRUN_AUDIT_LOG_ONLY&quot; |



## Enum: EvaluationModeEnum

| Name | Value |
|---- | -----|
| EVALUATION_MODE_UNSPECIFIED | &quot;EVALUATION_MODE_UNSPECIFIED&quot; |
| ALWAYS_ALLOW | &quot;ALWAYS_ALLOW&quot; |
| REQUIRE_ATTESTATION | &quot;REQUIRE_ATTESTATION&quot; |
| ALWAYS_DENY | &quot;ALWAYS_DENY&quot; |



