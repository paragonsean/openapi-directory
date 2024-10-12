

# UpdateOrganizationAdaptivePolicyGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the group |  [optional] |
|**name** | **String** | Name of the group |  [optional] |
|**policyObjects** | [**List&lt;CreateOrganizationAdaptivePolicyGroupRequestPolicyObjectsInner&gt;**](CreateOrganizationAdaptivePolicyGroupRequestPolicyObjectsInner.md) | The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group&#39;s SGT value if no other tagging scheme is being used (each requires one unique attribute) |  [optional] |
|**sgt** | **Integer** | SGT value of the group |  [optional] |



