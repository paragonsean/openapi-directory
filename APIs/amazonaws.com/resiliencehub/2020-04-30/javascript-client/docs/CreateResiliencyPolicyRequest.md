# AwsResilienceHub.CreateResiliencyPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. | [optional] 
**dataLocationConstraint** | **String** | Specifies a high-level geographical location constraint for where your resilience policy data can be stored. | [optional] 
**policy** | [**{String: FailurePolicy}**](FailurePolicy.md) | The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds. | 
**policyDescription** | **String** | The description for the policy. | [optional] 
**policyName** | **String** | The name of the policy | 
**tags** | **{String: String}** | Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair. | [optional] 
**tier** | **String** | The tier for this resiliency policy, ranging from the highest severity (&lt;code&gt;MissionCritical&lt;/code&gt;) to lowest (&lt;code&gt;NonCritical&lt;/code&gt;). | 



## Enum: DataLocationConstraintEnum


* `AnyLocation` (value: `"AnyLocation"`)

* `SameContinent` (value: `"SameContinent"`)

* `SameCountry` (value: `"SameCountry"`)





## Enum: TierEnum


* `MissionCritical` (value: `"MissionCritical"`)

* `Critical` (value: `"Critical"`)

* `Important` (value: `"Important"`)

* `CoreServices` (value: `"CoreServices"`)

* `NonCritical` (value: `"NonCritical"`)

* `NotApplicable` (value: `"NotApplicable"`)




