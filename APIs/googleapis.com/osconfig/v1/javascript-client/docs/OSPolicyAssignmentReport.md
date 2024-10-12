# OsConfigApi.OSPolicyAssignmentReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **String** | The Compute Engine VM instance name. | [optional] 
**lastRunId** | **String** | Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM. This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs. | [optional] 
**name** | **String** | The &#x60;OSPolicyAssignmentReport&#x60; API resource name. Format: &#x60;projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{os_policy_assignment_id}/report&#x60; | [optional] 
**osPolicyAssignment** | **String** | Reference to the &#x60;OSPolicyAssignment&#x60; API resource that the &#x60;OSPolicy&#x60; belongs to. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}&#x60; | [optional] 
**osPolicyCompliances** | [**[OSPolicyAssignmentReportOSPolicyCompliance]**](OSPolicyAssignmentReportOSPolicyCompliance.md) | Compliance data for each &#x60;OSPolicy&#x60; that is applied to the VM. | [optional] 
**updateTime** | **String** | Timestamp for when the report was last generated. | [optional] 


