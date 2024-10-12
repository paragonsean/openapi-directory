

# StackSet

A structure that contains information about a stack set. A stack set enables you to provision stacks into Amazon Web Services accounts and across Regions by using a single CloudFormation template. In the stack set, you specify the template to use, in addition to any parameters and capabilities that the template requires.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stackSetName** | [**String**](String.md) |  |  [optional] |
|**stackSetId** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**status** | [**StackSetStatus**](StackSetStatus.md) |  |  [optional] |
|**templateBody** | [**String**](String.md) |  |  [optional] |
|**parameters** | [**List**](List.md) |  |  [optional] |
|**capabilities** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**stackSetARN** | [**String**](String.md) |  |  [optional] |
|**administrationRoleARN** | [**String**](String.md) |  |  [optional] |
|**executionRoleName** | [**String**](String.md) |  |  [optional] |
|**stackSetDriftDetectionDetails** | [**StackSetStackSetDriftDetectionDetails**](StackSetStackSetDriftDetectionDetails.md) |  |  [optional] |
|**autoDeployment** | [**StackSetAutoDeployment**](StackSetAutoDeployment.md) |  |  [optional] |
|**permissionModel** | [**PermissionModels**](PermissionModels.md) |  |  [optional] |
|**organizationalUnitIds** | [**List**](List.md) |  |  [optional] |
|**managedExecution** | [**CreateStackSetInputManagedExecution**](CreateStackSetInputManagedExecution.md) |  |  [optional] |
|**regions** | [**List**](List.md) |  |  [optional] |



