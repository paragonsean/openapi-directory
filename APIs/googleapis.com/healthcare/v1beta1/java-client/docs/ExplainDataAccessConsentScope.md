

# ExplainDataAccessConsentScope

A single consent scope that provides info on who has access to the requested resource scope for a particular purpose and environment, enforced by which consent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessorScope** | [**ConsentAccessorScope**](ConsentAccessorScope.md) |  |  [optional] |
|**decision** | [**DecisionEnum**](#DecisionEnum) | Whether the current consent scope is permitted or denied access on the requested resource. |  [optional] |
|**enforcingConsents** | [**List&lt;ExplainDataAccessConsentInfo&gt;**](ExplainDataAccessConsentInfo.md) | Metadata of the consent resources that enforce the consent scope&#39;s access. |  [optional] |
|**exceptions** | [**List&lt;ExplainDataAccessConsentScope&gt;**](ExplainDataAccessConsentScope.md) | Other consent scopes that created exceptions within this scope. |  [optional] |



## Enum: DecisionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONSENT_DECISION_TYPE_UNSPECIFIED&quot; |
| PERMIT | &quot;CONSENT_DECISION_TYPE_PERMIT&quot; |
| DENY | &quot;CONSENT_DECISION_TYPE_DENY&quot; |



