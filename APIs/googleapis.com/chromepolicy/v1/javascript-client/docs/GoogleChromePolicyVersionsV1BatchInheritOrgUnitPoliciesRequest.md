# ChromePolicyApi.GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**[GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest]**](GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest.md) | List of policies that have to inherit their values as defined by the &#x60;requests&#x60;. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All &#x60;policyTargetKey.targetResource&#x60; values must point to an org unit resource. 3. All &#x60;policyTargetKey&#x60; values must have the same key names in the &#x60; additionalTargetKeys&#x60;. This also means if one of the targets has an empty &#x60;additionalTargetKeys&#x60; map, all of the targets must have an empty &#x60;additionalTargetKeys&#x60; map. 4. No two modification requests can reference the same &#x60;policySchema&#x60; + &#x60; policyTargetKey&#x60; pair.  | [optional] 


