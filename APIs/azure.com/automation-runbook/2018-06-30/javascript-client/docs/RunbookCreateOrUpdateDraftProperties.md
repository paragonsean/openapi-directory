# AutomationManagement.RunbookCreateOrUpdateDraftProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Gets or sets the description of the runbook. | [optional] 
**draft** | [**RunbookDraft**](RunbookDraft.md) |  | 
**logActivityTrace** | **Number** | Gets or sets the activity-level tracing options of the runbook. | [optional] 
**logProgress** | **Boolean** | Gets or sets progress log option. | [optional] 
**logVerbose** | **Boolean** | Gets or sets verbose log option. | [optional] 
**runbookType** | **String** | Gets or sets the type of the runbook. | 



## Enum: RunbookTypeEnum


* `Script` (value: `"Script"`)

* `Graph` (value: `"Graph"`)

* `PowerShellWorkflow` (value: `"PowerShellWorkflow"`)

* `PowerShell` (value: `"PowerShell"`)

* `GraphPowerShellWorkflow` (value: `"GraphPowerShellWorkflow"`)

* `GraphPowerShell` (value: `"GraphPowerShell"`)




