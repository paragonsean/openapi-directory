

# GoogleCloudPolicysimulatorV1OrgPolicyOverlay

The proposed changes to OrgPolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customConstraints** | [**List&lt;GoogleCloudPolicysimulatorV1OrgPolicyOverlayCustomConstraintOverlay&gt;**](GoogleCloudPolicysimulatorV1OrgPolicyOverlayCustomConstraintOverlay.md) | Optional. The OrgPolicy CustomConstraint changes to preview violations for. Any existing CustomConstraints with the same name will be overridden in the simulation. That is, violations will be determined as if all custom constraints in the overlay were instantiated. Only a single custom_constraint is supported in the overlay at a time. For evaluating multiple constraints, multiple &#x60;GenerateOrgPolicyViolationsPreview&#x60; requests are made, where each request evaluates a single constraint. |  [optional] |
|**policies** | [**List&lt;GoogleCloudPolicysimulatorV1OrgPolicyOverlayPolicyOverlay&gt;**](GoogleCloudPolicysimulatorV1OrgPolicyOverlayPolicyOverlay.md) | Optional. The OrgPolicy changes to preview violations for. Any existing OrgPolicies with the same name will be overridden in the simulation. That is, violations will be determined as if all policies in the overlay were created or updated. |  [optional] |



