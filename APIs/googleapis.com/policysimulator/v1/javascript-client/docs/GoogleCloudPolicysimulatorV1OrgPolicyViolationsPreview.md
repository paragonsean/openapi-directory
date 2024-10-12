# PolicySimulatorApi.GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when this &#x60;OrgPolicyViolationsPreview&#x60; was created. | [optional] [readonly] 
**customConstraints** | **[String]** | Output only. The names of the constraints against which all &#x60;OrgPolicyViolations&#x60; were evaluated. If &#x60;OrgPolicyOverlay&#x60; only contains &#x60;PolicyOverlay&#x60; then it contains the name of the configured custom constraint, applicable to the specified policies. Otherwise it contains the name of the constraint specified in &#x60;CustomConstraintOverlay&#x60;. Format: &#x60;organizations/{organization_id}/customConstraints/{custom_constraint_id}&#x60; Example: &#x60;organizations/123/customConstraints/custom.createOnlyE2TypeVms&#x60; | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the &#x60;OrgPolicyViolationsPreview&#x60;. It has the following format: &#x60;organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview}&#x60; Example: &#x60;organizations/my-example-org/locations/global/orgPolicyViolationsPreviews/506a5f7f&#x60; | [optional] [readonly] 
**overlay** | [**GoogleCloudPolicysimulatorV1OrgPolicyOverlay**](GoogleCloudPolicysimulatorV1OrgPolicyOverlay.md) |  | [optional] 
**resourceCounts** | [**GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreviewResourceCounts**](GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreviewResourceCounts.md) |  | [optional] 
**state** | **String** | Output only. The state of the &#x60;OrgPolicyViolationsPreview&#x60;. | [optional] [readonly] 
**violationsCount** | **Number** | Output only. The number of OrgPolicyViolations in this &#x60;OrgPolicyViolationsPreview&#x60;. This count may differ from &#x60;resource_summary.noncompliant_count&#x60; because each OrgPolicyViolation is specific to a resource **and** constraint. If there are multiple constraints being evaluated (i.e. multiple policies in the overlay), a single resource may violate multiple constraints. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"PREVIEW_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PREVIEW_PENDING"`)

* `RUNNING` (value: `"PREVIEW_RUNNING"`)

* `SUCCEEDED` (value: `"PREVIEW_SUCCEEDED"`)

* `FAILED` (value: `"PREVIEW_FAILED"`)




