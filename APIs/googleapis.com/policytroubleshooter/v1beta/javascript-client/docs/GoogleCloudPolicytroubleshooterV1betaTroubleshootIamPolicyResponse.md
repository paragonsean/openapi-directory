# PolicyTroubleshooterApi.GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Indicates whether the member has the specified permission for the specified resource, based on evaluating all of the applicable policies. | [optional] 
**explainedPolicies** | [**[GoogleCloudPolicytroubleshooterV1betaExplainedPolicy]**](GoogleCloudPolicytroubleshooterV1betaExplainedPolicy.md) | List of IAM policies that were evaluated to check the member&#39;s permissions, with annotations to indicate how each policy contributed to the final result. The list of policies can include the policy for the resource itself. It can also include policies that are inherited from higher levels of the resource hierarchy, including the organization, the folder, and the project. To learn more about the resource hierarchy, see https://cloud.google.com/iam/help/resource-hierarchy. | [optional] 



## Enum: AccessEnum


* `ACCESS_STATE_UNSPECIFIED` (value: `"ACCESS_STATE_UNSPECIFIED"`)

* `GRANTED` (value: `"GRANTED"`)

* `NOT_GRANTED` (value: `"NOT_GRANTED"`)

* `UNKNOWN_CONDITIONAL` (value: `"UNKNOWN_CONDITIONAL"`)

* `UNKNOWN_INFO_DENIED` (value: `"UNKNOWN_INFO_DENIED"`)




