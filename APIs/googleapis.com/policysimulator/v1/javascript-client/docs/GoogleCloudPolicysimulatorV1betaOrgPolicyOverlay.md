# PolicySimulatorApi.GoogleCloudPolicysimulatorV1betaOrgPolicyOverlay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customConstraints** | [**[GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay]**](GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay.md) | Optional. The OrgPolicy CustomConstraint changes to preview violations for. Any existing CustomConstraints with the same name will be overridden in the simulation. That is, violations will be determined as if all custom constraints in the overlay were instantiated. Only a single custom_constraint is supported in the overlay at a time. For evaluating multiple constraints, multiple &#x60;GenerateOrgPolicyViolationsPreview&#x60; requests are made, where each request evaluates a single constraint. | [optional] 
**policies** | [**[GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay]**](GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay.md) | Optional. The OrgPolicy changes to preview violations for. Any existing OrgPolicies with the same name will be overridden in the simulation. That is, violations will be determined as if all policies in the overlay were created or updated. | [optional] 


