# AutomationManagement.RunbookProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | Gets or sets the creation time. | [optional] 
**description** | **String** | Gets or sets the description. | [optional] 
**draft** | [**RunbookDraft**](RunbookDraft.md) |  | [optional] 
**jobCount** | **Number** | Gets or sets the job count of the runbook. | [optional] 
**lastModifiedBy** | **String** | Gets or sets the last modified by. | [optional] 
**lastModifiedTime** | **Date** | Gets or sets the last modified time. | [optional] 
**logActivityTrace** | **Number** | Gets or sets the option to log activity trace of the runbook. | [optional] 
**logProgress** | **Boolean** | Gets or sets progress log option. | [optional] 
**logVerbose** | **Boolean** | Gets or sets verbose log option. | [optional] 
**outputTypes** | **[String]** | Gets or sets the runbook output types. | [optional] 
**parameters** | [**{String: RunbookParameter}**](RunbookParameter.md) | Gets or sets the runbook parameters. | [optional] 
**provisioningState** | **String** | Gets or sets the provisioning state of the runbook. | [optional] 
**publishContentLink** | [**ContentLink**](ContentLink.md) |  | [optional] 
**runbookType** | **String** | Gets or sets the type of the runbook. | [optional] 
**state** | **String** | Gets or sets the state of the runbook. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)





## Enum: RunbookTypeEnum


* `Script` (value: `"Script"`)

* `Graph` (value: `"Graph"`)

* `PowerShellWorkflow` (value: `"PowerShellWorkflow"`)

* `PowerShell` (value: `"PowerShell"`)

* `GraphPowerShellWorkflow` (value: `"GraphPowerShellWorkflow"`)

* `GraphPowerShell` (value: `"GraphPowerShell"`)





## Enum: StateEnum


* `New` (value: `"New"`)

* `Edit` (value: `"Edit"`)

* `Published` (value: `"Published"`)




