

# CVSSv3

Common Vulnerability Scoring System version 3. For details, see https://www.first.org/cvss/specification-document

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attackComplexity** | [**AttackComplexityEnum**](#AttackComplexityEnum) | This metric describes the conditions beyond the attacker&#39;s control that must exist in order to exploit the vulnerability. |  [optional] |
|**attackVector** | [**AttackVectorEnum**](#AttackVectorEnum) | This metric reflects the context by which vulnerability exploitation is possible. |  [optional] |
|**availabilityImpact** | [**AvailabilityImpactEnum**](#AvailabilityImpactEnum) | This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability. |  [optional] |
|**baseScore** | **Float** | The base score is a function of the base metric scores. https://www.first.org/cvss/specification-document#Base-Metrics |  [optional] |
|**confidentialityImpact** | [**ConfidentialityImpactEnum**](#ConfidentialityImpactEnum) | This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. |  [optional] |
|**exploitabilityScore** | **Float** | The Exploitability sub-score equation is derived from the Base Exploitability metrics. https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics |  [optional] |
|**impactScore** | **Float** | The Impact sub-score equation is derived from the Base Impact metrics. |  [optional] |
|**integrityImpact** | [**IntegrityImpactEnum**](#IntegrityImpactEnum) | This metric measures the impact to integrity of a successfully exploited vulnerability. |  [optional] |
|**privilegesRequired** | [**PrivilegesRequiredEnum**](#PrivilegesRequiredEnum) | This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope. |  [optional] |
|**userInteraction** | [**UserInteractionEnum**](#UserInteractionEnum) | This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. |  [optional] |



## Enum: AttackComplexityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ATTACK_COMPLEXITY_UNSPECIFIED&quot; |
| LOW | &quot;ATTACK_COMPLEXITY_LOW&quot; |
| HIGH | &quot;ATTACK_COMPLEXITY_HIGH&quot; |



## Enum: AttackVectorEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ATTACK_VECTOR_UNSPECIFIED&quot; |
| NETWORK | &quot;ATTACK_VECTOR_NETWORK&quot; |
| ADJACENT | &quot;ATTACK_VECTOR_ADJACENT&quot; |
| LOCAL | &quot;ATTACK_VECTOR_LOCAL&quot; |
| PHYSICAL | &quot;ATTACK_VECTOR_PHYSICAL&quot; |



## Enum: AvailabilityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |



## Enum: ConfidentialityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |



## Enum: IntegrityImpactEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPACT_UNSPECIFIED&quot; |
| HIGH | &quot;IMPACT_HIGH&quot; |
| LOW | &quot;IMPACT_LOW&quot; |
| NONE | &quot;IMPACT_NONE&quot; |



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



