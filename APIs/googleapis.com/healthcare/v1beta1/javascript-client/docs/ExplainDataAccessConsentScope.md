# CloudHealthcareApi.ExplainDataAccessConsentScope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessorScope** | [**ConsentAccessorScope**](ConsentAccessorScope.md) |  | [optional] 
**decision** | **String** | Whether the current consent scope is permitted or denied access on the requested resource. | [optional] 
**enforcingConsents** | [**[ExplainDataAccessConsentInfo]**](ExplainDataAccessConsentInfo.md) | Metadata of the consent resources that enforce the consent scope&#39;s access. | [optional] 
**exceptions** | [**[ExplainDataAccessConsentScope]**](ExplainDataAccessConsentScope.md) | Other consent scopes that created exceptions within this scope. | [optional] 



## Enum: DecisionEnum


* `UNSPECIFIED` (value: `"CONSENT_DECISION_TYPE_UNSPECIFIED"`)

* `PERMIT` (value: `"CONSENT_DECISION_TYPE_PERMIT"`)

* `DENY` (value: `"CONSENT_DECISION_TYPE_DENY"`)




