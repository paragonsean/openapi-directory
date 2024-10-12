# OsConfigApi.CVSSv3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackComplexity** | **String** | This metric describes the conditions beyond the attacker&#39;s control that must exist in order to exploit the vulnerability. | [optional] 
**attackVector** | **String** | This metric reflects the context by which vulnerability exploitation is possible. | [optional] 
**availabilityImpact** | **String** | This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability. | [optional] 
**baseScore** | **Number** | The base score is a function of the base metric scores. https://www.first.org/cvss/specification-document#Base-Metrics | [optional] 
**confidentialityImpact** | **String** | This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. | [optional] 
**exploitabilityScore** | **Number** | The Exploitability sub-score equation is derived from the Base Exploitability metrics. https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics | [optional] 
**impactScore** | **Number** | The Impact sub-score equation is derived from the Base Impact metrics. | [optional] 
**integrityImpact** | **String** | This metric measures the impact to integrity of a successfully exploited vulnerability. | [optional] 
**privilegesRequired** | **String** | This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. | [optional] 
**scope** | **String** | The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope. | [optional] 
**userInteraction** | **String** | This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. | [optional] 



## Enum: AttackComplexityEnum


* `UNSPECIFIED` (value: `"ATTACK_COMPLEXITY_UNSPECIFIED"`)

* `LOW` (value: `"ATTACK_COMPLEXITY_LOW"`)

* `HIGH` (value: `"ATTACK_COMPLEXITY_HIGH"`)





## Enum: AttackVectorEnum


* `UNSPECIFIED` (value: `"ATTACK_VECTOR_UNSPECIFIED"`)

* `NETWORK` (value: `"ATTACK_VECTOR_NETWORK"`)

* `ADJACENT` (value: `"ATTACK_VECTOR_ADJACENT"`)

* `LOCAL` (value: `"ATTACK_VECTOR_LOCAL"`)

* `PHYSICAL` (value: `"ATTACK_VECTOR_PHYSICAL"`)





## Enum: AvailabilityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)





## Enum: ConfidentialityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)





## Enum: IntegrityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)





## Enum: PrivilegesRequiredEnum


* `UNSPECIFIED` (value: `"PRIVILEGES_REQUIRED_UNSPECIFIED"`)

* `NONE` (value: `"PRIVILEGES_REQUIRED_NONE"`)

* `LOW` (value: `"PRIVILEGES_REQUIRED_LOW"`)

* `HIGH` (value: `"PRIVILEGES_REQUIRED_HIGH"`)





## Enum: ScopeEnum


* `UNSPECIFIED` (value: `"SCOPE_UNSPECIFIED"`)

* `UNCHANGED` (value: `"SCOPE_UNCHANGED"`)

* `CHANGED` (value: `"SCOPE_CHANGED"`)





## Enum: UserInteractionEnum


* `UNSPECIFIED` (value: `"USER_INTERACTION_UNSPECIFIED"`)

* `NONE` (value: `"USER_INTERACTION_NONE"`)

* `REQUIRED` (value: `"USER_INTERACTION_REQUIRED"`)




