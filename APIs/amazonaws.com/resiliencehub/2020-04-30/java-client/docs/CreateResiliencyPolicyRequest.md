

# CreateResiliencyPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. |  [optional] |
|**dataLocationConstraint** | [**DataLocationConstraintEnum**](#DataLocationConstraintEnum) | Specifies a high-level geographical location constraint for where your resilience policy data can be stored. |  [optional] |
|**policy** | [**Map&lt;String, FailurePolicy&gt;**](FailurePolicy.md) | The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds. |  |
|**policyDescription** | **String** | The description for the policy. |  [optional] |
|**policyName** | **String** | The name of the policy |  |
|**tags** | **Map&lt;String, String&gt;** | Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier for this resiliency policy, ranging from the highest severity (&lt;code&gt;MissionCritical&lt;/code&gt;) to lowest (&lt;code&gt;NonCritical&lt;/code&gt;). |  |



## Enum: DataLocationConstraintEnum

| Name | Value |
|---- | -----|
| ANY_LOCATION | &quot;AnyLocation&quot; |
| SAME_CONTINENT | &quot;SameContinent&quot; |
| SAME_COUNTRY | &quot;SameCountry&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| MISSION_CRITICAL | &quot;MissionCritical&quot; |
| CRITICAL | &quot;Critical&quot; |
| IMPORTANT | &quot;Important&quot; |
| CORE_SERVICES | &quot;CoreServices&quot; |
| NON_CRITICAL | &quot;NonCritical&quot; |
| NOT_APPLICABLE | &quot;NotApplicable&quot; |



