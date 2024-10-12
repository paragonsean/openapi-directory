

# GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest

Request message for modifying multiple policy values for a specific group-based target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest&gt;**](GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest.md) | List of policies to modify as defined by the &#x60;requests&#x60;. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All &#x60;policyTargetKey.targetResource&#x60; values must point to a group resource. 3. All &#x60;policyTargetKey&#x60; values must have the same &#x60;app_id&#x60; key name in the &#x60;additionalTargetKeys&#x60;. 4. No two modification requests can reference the same &#x60;policySchema&#x60; + &#x60; policyTargetKey&#x60; pair.  |  [optional] |



