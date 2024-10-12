# PolicySimulatorApi.GoogleCloudPolicysimulatorV1OrgPolicyOverlay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customConstraints** | [**[GoogleCloudPolicysimulatorV1OrgPolicyOverlayCustomConstraintOverlay]**](GoogleCloudPolicysimulatorV1OrgPolicyOverlayCustomConstraintOverlay.md) | Optional. The OrgPolicy CustomConstraint changes to preview violations for. Any existing CustomConstraints with the same name will be overridden in the simulation. That is, violations will be determined as if all custom constraints in the overlay were instantiated. Only a single custom_constraint is supported in the overlay at a time. For evaluating multiple constraints, multiple &#x60;GenerateOrgPolicyViolationsPreview&#x60; requests are made, where each request evaluates a single constraint. | [optional] 
**policies** | [**[GoogleCloudPolicysimulatorV1OrgPolicyOverlayPolicyOverlay]**](GoogleCloudPolicysimulatorV1OrgPolicyOverlayPolicyOverlay.md) | Optional. The OrgPolicy changes to preview violations for. Any existing OrgPolicies with the same name will be overridden in the simulation. That is, violations will be determined as if all policies in the overlay were created or updated. | [optional] 


