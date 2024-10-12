# ContainerAnalysisApi.CVSS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackComplexity** | **String** |  | [optional] 
**attackVector** | **String** | Base Metrics Represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments. | [optional] 
**authentication** | **String** |  | [optional] 
**availabilityImpact** | **String** |  | [optional] 
**baseScore** | **Number** | The base score is a function of the base metric scores. | [optional] 
**confidentialityImpact** | **String** |  | [optional] 
**exploitabilityScore** | **Number** |  | [optional] 
**impactScore** | **Number** |  | [optional] 
**integrityImpact** | **String** |  | [optional] 
**privilegesRequired** | **String** |  | [optional] 
**scope** | **String** |  | [optional] 
**userInteraction** | **String** |  | [optional] 



## Enum: AttackComplexityEnum


* `UNSPECIFIED` (value: `"ATTACK_COMPLEXITY_UNSPECIFIED"`)

* `LOW` (value: `"ATTACK_COMPLEXITY_LOW"`)

* `HIGH` (value: `"ATTACK_COMPLEXITY_HIGH"`)

* `MEDIUM` (value: `"ATTACK_COMPLEXITY_MEDIUM"`)





## Enum: AttackVectorEnum


* `UNSPECIFIED` (value: `"ATTACK_VECTOR_UNSPECIFIED"`)

* `NETWORK` (value: `"ATTACK_VECTOR_NETWORK"`)

* `ADJACENT` (value: `"ATTACK_VECTOR_ADJACENT"`)

* `LOCAL` (value: `"ATTACK_VECTOR_LOCAL"`)

* `PHYSICAL` (value: `"ATTACK_VECTOR_PHYSICAL"`)





## Enum: AuthenticationEnum


* `UNSPECIFIED` (value: `"AUTHENTICATION_UNSPECIFIED"`)

* `MULTIPLE` (value: `"AUTHENTICATION_MULTIPLE"`)

* `SINGLE` (value: `"AUTHENTICATION_SINGLE"`)

* `NONE` (value: `"AUTHENTICATION_NONE"`)





## Enum: AvailabilityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)

* `PARTIAL` (value: `"IMPACT_PARTIAL"`)

* `COMPLETE` (value: `"IMPACT_COMPLETE"`)





## Enum: ConfidentialityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)

* `PARTIAL` (value: `"IMPACT_PARTIAL"`)

* `COMPLETE` (value: `"IMPACT_COMPLETE"`)





## Enum: IntegrityImpactEnum


* `UNSPECIFIED` (value: `"IMPACT_UNSPECIFIED"`)

* `HIGH` (value: `"IMPACT_HIGH"`)

* `LOW` (value: `"IMPACT_LOW"`)

* `NONE` (value: `"IMPACT_NONE"`)

* `PARTIAL` (value: `"IMPACT_PARTIAL"`)

* `COMPLETE` (value: `"IMPACT_COMPLETE"`)





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




