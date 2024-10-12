

# AnalyzerOrgPolicy

This organization policy message is a modified version of the one defined in the Organization Policy system. This message contains several fields defined in the original organization policy with some new fields for analysis purpose.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedResource** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to. For any user defined org policies, this field has the same value as the [attached_resource] field. Only for default policy, this field has the different value. |  [optional] |
|**attachedResource** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set. Notice that some type of constraints are defined with default policy. This field will be empty for them. |  [optional] |
|**inheritFromParent** | **Boolean** | If &#x60;inherit_from_parent&#x60; is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation. |  [optional] |
|**reset** | **Boolean** | Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, &#x60;rules&#x60; must be empty and &#x60;inherit_from_parent&#x60; must be set to false. |  [optional] |
|**rules** | [**List&lt;GoogleCloudAssetV1Rule&gt;**](GoogleCloudAssetV1Rule.md) | List of rules for this organization policy. |  [optional] |



