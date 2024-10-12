

# CVSS

Common Vulnerability Scoring System. This message is compatible with CVSS v2 and v3. For CVSS v2 details, see https://www.first.org/cvss/v2/guide CVSS v2 calculator: https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator For CVSS v3 details, see https://www.first.org/cvss/specification-document CVSS v3 calculator: https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attackComplexity** | [**AttackComplexityEnum**](#AttackComplexityEnum) | Defined in CVSS v3, CVSS v2 |  [optional] |
|**attackVector** | [**AttackVectorEnum**](#AttackVectorEnum) | Base Metrics Represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments. Defined in CVSS v3, CVSS v2 |  [optional] |
|**authentication** | [**AuthenticationEnum**](#AuthenticationEnum) | Defined in CVSS v2 |  [optional] |
|**availabilityImpact** | [**AvailabilityImpactEnum**](#AvailabilityImpactEnum) | Defined in CVSS v3, CVSS v2 |  [optional] |
|**baseScore** | **Float** | The base score is a function of the base metric scores. |  [optional] |
|**confidentialityImpact** | [**ConfidentialityImpactEnum**](#ConfidentialityImpactEnum) | Defined in CVSS v3, CVSS v2 |  [optional] |
|**exploitabilityScore** | **Float** |  |  [optional] |
|**impactScore** | **Float** |  |  [optional] |
|**integrityImpact** | [**IntegrityImpactEnum**](#IntegrityImpactEnum) | Defined in CVSS v3, CVSS v2 |  [optional] |
|**privilegesRequired** | [**PrivilegesRequiredEnum**](#PrivilegesRequiredEnum) | Defined in CVSS v3 |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Defined in CVSS v3 |  [optional] |
|**userInteraction** | [**UserInteractionEnum**](#UserInteractionEnum) | Defined in CVSS v3 |  [optional] |



## Enum: AttackComplexityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ATTACK_COMPLEXITY_UNSPECIFIED&quot; |
| LOW | &quot;ATTACK_COMPLEXITY_LOW&quot; |
| HIGH | &quot;ATTACK_COMPLEXITY_HIGH&quot; |
| MEDIUM | &quot;ATTACK_COMPLEXITY_MEDIUM&quot; |



## Enum: AttackVectorEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ATTACK_VECTOR_UNSPECIFIED&quot; |
| NETWORK | &quot;ATTACK_VECTOR_NETWORK&quot; |
| ADJACENT | &quot;ATTACK_VECTOR_ADJACENT&quot; |
| LOCAL | &quot;ATTACK_VECTOR_LOCAL&quot; |
| PHYSICAL | &quot;ATTACK_VECTOR_PHYSICAL&quot; |



## Enum: AuthenticationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTHENTICATION_UNSPECIFIED&quot; |
| MULTIPLE | &quot;AUTHENTICATION_MULTIPLE&quot; |
| SINGLE | &quot;AUTHENTICATION_SINGLE&quot; |
| NONE | &quot;AUTHENTICATION_NONE&quot; |



## Enum: AvailabilityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |
| PARTIAL | &quot;IMPACT_PARTIAL&quot; |
| COMPLETE | &quot;IMPACT_COMPLETE&quot; |



## Enum: ConfidentialityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |
| PARTIAL | &quot;IMPACT_PARTIAL&quot; |
| COMPLETE | &quot;IMPACT_COMPLETE&quot; |



## Enum: IntegrityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |
| PARTIAL | &quot;IMPACT_PARTIAL&quot; |
| COMPLETE | &quot;IMPACT_COMPLETE&quot; |



## Enum: PrivilegesRequiredEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRIVILEGES_REQUIRED_UNSPECIFIED&quot; |
| NONE | &quot;PRIVILEGES_REQUIRED_NONE&quot; |
| LOW | &quot;PRIVILEGES_REQUIRED_LOW&quot; |
| HIGH | &quot;PRIVILEGES_REQUIRED_HIGH&quot; |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SCOPE_UNSPECIFIED&quot; |
| UNCHANGED | &quot;SCOPE_UNCHANGED&quot; |
| CHANGED | &quot;SCOPE_CHANGED&quot; |



## Enum: UserInteractionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;USER_INTERACTION_UNSPECIFIED&quot; |
| NONE | &quot;USER_INTERACTION_NONE&quot; |
| REQUIRED | &quot;USER_INTERACTION_REQUIRED&quot; |



