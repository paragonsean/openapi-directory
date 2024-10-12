# ContainerAnalysisApi.CVSSv3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attackComplexity** | **String** |  | [optional] 
**attackVector** | **String** | Base Metrics Represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments. | [optional] 
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




