# BatchApi.AllocationPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**[InstancePolicyOrTemplate]**](InstancePolicyOrTemplate.md) | Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now. | [optional] 
**labels** | **{String: String}** | Labels applied to all VM instances and other resources created by AllocationPolicy. Labels could be user provided or system generated. You can assign up to 64 labels. [Google Compute Engine label restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) apply. Label names that start with \&quot;goog-\&quot; or \&quot;google-\&quot; are reserved. | [optional] 
**location** | [**LocationPolicy**](LocationPolicy.md) |  | [optional] 
**network** | [**NetworkPolicy**](NetworkPolicy.md) |  | [optional] 
**placement** | [**PlacementPolicy**](PlacementPolicy.md) |  | [optional] 
**serviceAccount** | [**ServiceAccount**](ServiceAccount.md) |  | [optional] 
**tags** | **[String]** | Optional. Tags applied to the VM instances. The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). | [optional] 


