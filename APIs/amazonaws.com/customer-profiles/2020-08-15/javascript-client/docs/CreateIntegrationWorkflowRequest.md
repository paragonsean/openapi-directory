# AmazonConnectCustomerProfiles.CreateIntegrationWorkflowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflowType** | **String** | The type of workflow. The only supported value is APPFLOW_INTEGRATION. | 
**integrationConfig** | [**CreateIntegrationWorkflowRequestIntegrationConfig**](CreateIntegrationWorkflowRequestIntegrationConfig.md) |  | 
**objectTypeName** | **String** | The name of the profile object type. | 
**roleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution. | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 



## Enum: WorkflowTypeEnum


* `APPFLOW_INTEGRATION` (value: `"APPFLOW_INTEGRATION"`)




