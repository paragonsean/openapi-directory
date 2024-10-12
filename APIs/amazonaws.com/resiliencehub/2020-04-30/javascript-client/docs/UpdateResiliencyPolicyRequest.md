# AwsResilienceHub.UpdateResiliencyPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataLocationConstraint** | **String** | Specifies a high-level geographical location constraint for where your resilience policy data can be stored. | [optional] 
**policy** | [**{String: FailurePolicy}**](FailurePolicy.md) | The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds. | [optional] 
**policyArn** | **String** | Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:resiliency-policy/&lt;code&gt;policy-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | 
**policyDescription** | **String** | The description for the policy. | [optional] 
**policyName** | **String** | The name of the policy | [optional] 
**tier** | **String** | The tier for this resiliency policy, ranging from the highest severity (&lt;code&gt;MissionCritical&lt;/code&gt;) to lowest (&lt;code&gt;NonCritical&lt;/code&gt;). | [optional] 



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




