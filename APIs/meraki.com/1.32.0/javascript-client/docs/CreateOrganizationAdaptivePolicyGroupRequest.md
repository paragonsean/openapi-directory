# MerakiDashboardApi.CreateOrganizationAdaptivePolicyGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the group (default: \&quot;\&quot;) | [optional] 
**name** | **String** | Name of the group | 
**policyObjects** | [**[CreateOrganizationAdaptivePolicyGroupRequestPolicyObjectsInner]**](CreateOrganizationAdaptivePolicyGroupRequestPolicyObjectsInner.md) | The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group&#39;s SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: []) | [optional] 
**sgt** | **Number** | SGT value of the group | 


